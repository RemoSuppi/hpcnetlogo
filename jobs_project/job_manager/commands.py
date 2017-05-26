""" Main functionality """

import os
import paramiko

from django.template.loader import get_template

from django.template import Context

def run_command():
    """ This is dummy and does not do anything anymore in the code """
    return 'True'


def submit_job(job, hostname, username, password, model_name, cluster_number):
    """
    Executed when clicking the play button, the parameters are what passed
    from the interface to this function
    """
    # Directory of the split command. Change if necessary.    
    actual_dir = '/var/www/html/jobs_project/job_manager/'
    # Netlogo directory-version
    netlv = 'netlogo-5.2.1'
    # Cluster Queues names
    clusg = 'cluster.q@clus*.hpc.local'
    clus1 = 'cluster.q@clus'
    clus2 = '.hpc.local'

    try:

        try:
            expand = job.e_e
            #making a directory for splitted experiments, it is current directory/experiments
            xml_dir = os.path.join(os.path.dirname(job.file_first.path), 'experiments-%d-%d' % (job.id, job.latest_run))
            os.mkdir(xml_dir)

            #splitting the model using command line and piutting the result in xml_dir = current /experiments
            if expand:
                os.system(actual_dir + 'split_nlogo_experiment.py --repetitions_per_run 1 %s %s --output_dir %s' % (job.file_first.path, job.experiment_name, xml_dir))
            else:
                os.system(actual_dir+'split_nlogo_experiment.py %s %s --output_dir %s' % (job.file_first.path, job.experiment_name, xml_dir))
        
        except Exception as e_s:
            print('*** Caught Split exception: ' + str(e_s.__class__) + ': ' + str(e_s))

        #setting server (cluster master node) key directories
        netlogo_dir = '/home/%s/netlogo-sge' % username
        java_prefs_dir = '/home/%s/.java' % username
        # setting job-# directory and run, e.g. job-2/1
        run_dir = os.path.join(netlogo_dir, 'job-%s' % job.id, '%d' % job.latest_run)
        output_dir = os.path.join(run_dir, 'output')
        error_dir = os.path.join(run_dir, 'error')
        model_filepath = os.path.join(run_dir, os.path.split(job.file_first.path)[1])
        experiment_filepath = ''

        # login to master node
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname, username=username, password=password)

        s.exec_command('mkdir -p %s' % run_dir)
        # cd to run directory
        s.exec_command('cd %s' % run_dir)

        #copy experiment files to server
        for experiment_filename in os.listdir(xml_dir):
            file_path = os.path.join(xml_dir, experiment_filename)
            destination_path = os.path.join(run_dir, experiment_filename)
            copy_file(s, file_path, destination_path)

        experiments_count = len(os.listdir(xml_dir))

        # create output dir
        s.exec_command('mkdir -p %s' % output_dir)

        # create error dir
        s.exec_command('mkdir -p %s' % error_dir)

        simulator_name = 'run-simulator-%d-%d.sh' % (job.id, job.latest_run)

        # copy job submit script

        context_dict = {
            'experiment_name': job.experiment_name,
            'experiment_count': experiments_count,
            'work_dir': run_dir,
            'simulator_dir': run_dir,
            'netlogo_dir': os.path.join(netlogo_dir, netlv),
            'simulator_src_dir': run_dir,
            'output_dir': output_dir,
            'model_name': model_name,
            'error_dir': error_dir,
            'simulator_name': simulator_name,
        }

        if experiments_count < 10:
            job_submit_script = get_script('job-submit.sh', context_dict)
        elif experiments_count < 100:
            job_submit_script = get_script('job-submit0010.sh', context_dict)
        elif experiments_count < 1000:
            job_submit_script = get_script('job-submit0100.sh', context_dict)
        else:
            job_submit_script = get_script('job-submit1000.sh', context_dict)

        j_s = run_dir+'/job-submit.sh'
        copy_script(s, job_submit_script, j_s, xml_dir+'/job-submit.sh')
        s.exec_command('chmod +x %s' % j_s)

        # copy sge script
        if cluster_number == '*':
            cluster_string = clusg 
        else:
            cluster_string = clus1 + cluster_number + clus2
        context_dict = {
            'cluster_number': cluster_string,
            'work_dir': run_dir,
            'simulator_dir': run_dir,
            'netlogo_dir': os.path.join(netlogo_dir, netlv),
            'simulator_src_dir': run_dir,
            'output_dir': output_dir,
            'model_name': model_name,
            'error_dir': error_dir,
            'simulator_name': simulator_name,
        }
        sge_script = get_script('sge-script2.sh', context_dict)
        s_s = run_dir+'/sge-script2.sh'
        copy_script(s, sge_script, s_s, xml_dir+'/sge-script2.sh')
        s.exec_command('chmod +x %s' % s_s)

        # copy run simulator script

        context_dict = {
            'work_dir': run_dir,
            'model_file': model_filepath,
            'experiment_file': experiment_filepath,
            'netlogo_dir': os.path.join(netlogo_dir, netlv),
            'output_dir': output_dir,
            'java_prefs_dir': java_prefs_dir,
        }

        run_simulator_script = get_script('run-simulator.sh', context_dict)
        r_s = netlogo_dir + '/' + netlv
        r_version = 'run-simulator-%d-%d.sh' % (job.id, job.latest_run)
        copy_script(s, run_simulator_script, r_s + '/' + r_version, xml_dir+'/run-simulator-sh')
        s.exec_command('chmod +x %s' % r_s + '/' + r_version)

        # copy .nlogo file
        copy_file(s, job.file_first.path, model_filepath)

        # execute job-submit
        s.exec_command('/bin/bash %s/job-submit.sh >> %s/output.txt' % (run_dir, run_dir))
        s.exec_command('touch %s/ok' % run_dir)

        job.latest_run += 1
        job.save()

        s.close()
        return 'Successfully ran the job'

    except Exception as e:
        print('*** Caught Run Job exception: ' + str(e.__class__) + ': ' + str(e))

def get_script(script_name, context_dict={}):
    """ Get an Script & Context """
    template = get_template(script_name)
    context = Context(context_dict)
    return template.render(context)


def copy_file(ssh, local_filepath, remote_filepath):
    """ Copy a file """
    ftp = ssh.open_sftp()
    ftp.put(local_filepath, remote_filepath)


def copy_script(ssh, script, filename, local):
    """ Copy a Script """
    f = open(local, 'w')
    for line in script.split('\n'):
        f.write(line+'\n')
    f.close()
    copy_file(ssh, local, filename)


def stop_job(job, hostname, username, password):
    """ Stop a Job """
    try:
        # login to master node
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname, username=username, password=password)

	# send killall command - Warning: V.1.1 this will erase all the user's jobs.
	#Improvement: find the id and delete selectively.
        s.exec_command('qdel -u %s' % username)

        s.close()
        return 'Successfully stop job'

    except Exception as e:
        print('*** Caught Stop Job exception: ' + str(e.__class__) + ': ' + str(e))


