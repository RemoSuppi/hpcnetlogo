{% autoescape off %}
#!/bin/bash
# Version 0.4
start=$(date +%s.%N)

for ((i=0;i<{{experiment_count}};i++))
do
qsub {{work_dir}}/sge-script2.sh {{experiment_name}}$i.xml {{experiment_name}}$i.csv
done

end=$(date +%s.%N)
runtime=$(echo $end - $start | bc)
echo "Runtime was $runtime"
echo {{experiment_name}} $runtime >>output.txt



{% endautoescape %}
