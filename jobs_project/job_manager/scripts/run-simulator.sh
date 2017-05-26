{% autoescape off %}
# Version 0.1
startp=$(date +%s.%N)

echo $startp
java -Xmx2048m -XX:MaxPermSize=512m -Xms512m -Dfile.encoding=UTF-8  -Djava.util.prefs.userRoot={{ java_prefs_dir }} -cp NetLogo.jar org.nlogo.headless.Main --model {{ model_file }} --setup-file {{ work_dir }}/$1 --table {{ output_dir }}/$2 

#optional: --threads {{thread_count}


endp=$(date +%s.%N)
echo $endp

runtime=$(echo $endp - $startp | bc)

echo "Partial Runtime $1: $runtime"

{% endautoescape %}
