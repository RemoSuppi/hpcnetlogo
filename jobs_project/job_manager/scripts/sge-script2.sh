### Version 0.3
#$ -N {{ model_name }}
#$ -S /bin/bash
####$ -V
#$ -cwd
#$ -notify
#$ -o {{ output_dir }}
#$ -e {{ error_dir }}
#$ -m e

#$ -q {{cluster_number}}

###WORK_DIR={{ work_dir }}
###SIMULATOR_DIR={{ simulator_dir }}
NETLOGO_DIR={{ netlogo_dir }}
###SIMULATOR_SRC_DIR={{ simulator_src_dir }}

#execute
cd $NETLOGO_DIR
sh ./{{simulator_name}} $1 $2

exit 0
