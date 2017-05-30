
#!/bin/bash
# Version 0.4
start=$(date +%s.%N)

for ((i=0;i<3;i++))
do
qsub /home/netlogo/netlogo-sge/job-3/1/sge-script2.sh e1$i.xml e1$i.csv
done

end=$(date +%s.%N)
runtime=$(echo $end - $start | bc)
echo "Runtime was $runtime"
echo e1 $runtime >>output.txt





