# hpcnetlogo 
## License: GNU GLP 3

*Hpcnetlogo* is a frontend for the concurrent execution of **Netlogo** experiments defined in **Behavior Space** (BS). The goal of this environment is that non-technological users can use HPC to run their experiments in the BS without worrying about the configuration of SGE or Netlogo-Java.This environment sends the experiments to be executed to a cluster using SGE (but the scripts can be adapted for other queues systems such as SLURM).

This frontend uses: 
1. Netlogo Program (https://ccl.northwestern.edu/netlogo/5.2.1/) executed as headless in a cluster with SGE.
1. Split_nlogo_experiment (https://github.com/ahrenberg/split_nlogo_experiment) to create the xml files from Behavior Space.
1. Directory Lister (http://www.directorylister.com ) to show the output files (result of execution).

### VirtualBox Sandbox
1. Download hpcnetlogo VM for Virtualbox from [here](https://uab-my.sharepoint.com/personal/1004099_uab_cat/_layouts/15/guestaccess.aspx?docid=1fcbdba18f63b43a9902f75ef029f4af1&authkey=AUF8uTl3lJ7AR6PF_YEydow)
1. Import ova file in *File->Import Appliance* 
1. Start the VM
1. User & passwd (including root passwd): *hpcnetlogo*
1. Open the URL http://127.0.0.1 in a browser in the Host (there is a port forwarding from MV). 

### To install hpcnetlogo on Ubuntu 16.04LTS (a VirtualBox VM can be used):
1. Install base software 
```
apt-get install apache2 libssl-dev libapache2-mod-wsgi-py3 python3-django python3-pip
pip3 install paramiko
pip3 install django-bootstrap-form
rm /usr/bin/python
ln -s /usr/bin/python3.5 /usr/bin/python

```
2. Clone the repository:

```
git clone https://github.com/hpcnetlogo/hpcnetlogo.git
cd hpcnetlogo
mv jobs_project /var/www/html
chown www-data:www-data /var/www/html/jobs_project
mv 000-default.conf /etc/apache2/sites-available
systemctl restart apache2

```
3. Open a browser in http://127.0.0.1. 
If you use a MV (eg Virtualbox) without GUI in Linux, you can map the port 80 on NAT network adapter (Port Forwarding) to port 80 of the host and using the host browser in the same URL. For errors consult */var/log/apache2/error.log*.

* The user & passwd to upload files are **netlogo** for both. The Django Admin (http://127.0.0.1/admin) user & password are **hpcnetlogo** for both. The parameters of Upload experiment page are:
  * **Model**: the nlogo file with the BS experiment included.
  * **Experiment name**: the experiment name defined in the BS.
  * **Run separate repetitions?**: if marked the repetitions of the BS will be executed in a different node of the Sge cluster.
  * **Model name**: experiment name in SGE Cluster. 
  * **Cluster Queue: \*|Node_Number**: \* all nodes in the SGE cluster, Number of queue in the SGE cluster. 
  * **Hostname**: SGE submit node (name.domain or IP)
  * **Username**: user in the SGE cluster (access by SSH).
  * **Password**: passwd of the user in the SGE cluster.

4. In your SGE cluster: you need install Netlogo 5.2.1 program (from https://ccl.northwestern.edu/netlogo/5.2.1/) on a dedicated *user*, in the folder */home/user/netlogo-sge/netlogo-5.2.1*  (please use the same folders because its are included in the frontend scripts). Verify that you can access to this *user* by `ssh` from hpcnetlogo machine. If you change the directory o version of netlogo you need modifify this directory in *jobs_project/job_manager/commands.py* file and *jobs_project/job_manager/scripts*.

5. Hpcnetlogo uses **Directory Lister** (http://www.directorylister.com ) to show the output files of netlogo execution. Please install it in you master node of your cluster and add, in the installation directory, a link to */home/user/netlogo-sge*. Then you need modify the file *jobs_project/job_manager/templates/job_manager/job_list.html* to introduce the correct URL of your button Output for directory lister. 

* It is necessary to change the lines 25-27 of *jobs_project/job_manager/commands.py* in order to change the name of your queues (variable *cluster_string*) to adequate it to your queues names (in our system is cluster.q@clu\*.hpc.local). If you change the netlogo version or directories, please modify the scripts in the *jobs_project/job_manager/scripts* and line 23 of *jobs_project/job_manager/commands.py*. 


### Authors: Ghazal Tashakor (g.tashakor AT caos.uab.cat), Remo Suppi (Remo.Suppi AT uab.cat)
#### Research Group: http://grupsderecerca.uab.cat/hpc4eas/
#### License : GNU GLP 3



