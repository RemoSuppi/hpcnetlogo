### Version 0.3
#$ -N a
#$ -S /bin/bash
####$ -V
#$ -cwd
#$ -notify
#$ -o /home/netlogo/netlogo-sge/job-1/1/output
#$ -e /home/netlogo/netlogo-sge/job-1/1/error
#$ -m e

#$ -q cluster.q@clus8.hpc.local

###WORK_DIR=/home/netlogo/netlogo-sge/job-1/1
###SIMULATOR_DIR=/home/netlogo/netlogo-sge/job-1/1
NETLOGO_DIR=/home/netlogo/netlogo-sge/netlogo-5.2.1
###SIMULATOR_SRC_DIR=/home/netlogo/netlogo-sge/job-1/1

#execute
cd $NETLOGO_DIR
sh ./run-simulator-1-1.sh $1 $2

exit 0

