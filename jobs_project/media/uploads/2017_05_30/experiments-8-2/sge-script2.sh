### Version 0.3
#$ -N q
#$ -S /bin/bash
####$ -V
#$ -cwd
#$ -notify
#$ -o /home/netlogo/netlogo-sge/job-8/2/output
#$ -e /home/netlogo/netlogo-sge/job-8/2/error
#$ -m e

#$ -q cluster.q@clus8.hpc.local

###WORK_DIR=/home/netlogo/netlogo-sge/job-8/2
###SIMULATOR_DIR=/home/netlogo/netlogo-sge/job-8/2
NETLOGO_DIR=/home/netlogo/netlogo-sge/netlogo-5.2.1
###SIMULATOR_SRC_DIR=/home/netlogo/netlogo-sge/job-8/2

#execute
cd $NETLOGO_DIR
sh ./run-simulator-8-2.sh $1 $2

exit 0

