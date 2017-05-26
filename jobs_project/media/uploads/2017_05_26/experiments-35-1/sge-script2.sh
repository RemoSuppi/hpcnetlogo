### Version 0.3
#$ -N fv
#$ -S /bin/bash
####$ -V
#$ -cwd
#$ -notify
#$ -o /home/netlogo/netlogo-sge/job-35/1/output
#$ -e /home/netlogo/netlogo-sge/job-35/1/error
#$ -m e

#$ -q cluster.q@clus*.hpc.local

###WORK_DIR=/home/netlogo/netlogo-sge/job-35/1
###SIMULATOR_DIR=/home/netlogo/netlogo-sge/job-35/1
NETLOGO_DIR=/home/netlogo/netlogo-sge/netlogo-5.2.1
###SIMULATOR_SRC_DIR=/home/netlogo/netlogo-sge/job-35/1

#execute
cd $NETLOGO_DIR
sh ./run-simulator-35-1.sh $1 $2

exit 0

