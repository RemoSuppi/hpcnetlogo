{% autoescape off %}

start=$(date +%s.%N)

for ((i=0;i<10;i++))
do
qsub {{work_dir}}/sge-script2.sh {{experiment_name}}00$i.xml {{experiment_name}}00$i.csv
done

for ((i=10;i<100;i++))
do
qsub {{work_dir}}/sge-script2.sh {{experiment_name}}0$i.xml {{experiment_name}}0$i.csv
done

for ((i=100;i<{{experiment_count}};i++))
do
qsub {{work_dir}}sge-script2.sh {{experiment_name}}$i.xml {{experiment_name}}$i.csv
done

end=$(date +%s.%N)
runtime=$(echo $end - $start | bc)
echo "Runtime was $runtime"
echo {{experiment_name}} $runtime >>output.txt

{% endautoescape %}
