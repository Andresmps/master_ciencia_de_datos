# Comandos para ejecutar los jobs punto 2
---

Caso de prueba reducido:
```
cd punto2/src/
```
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-$HADOOP_VERSION.jar \
    -files ./mapper.py,./reducer.py \
    -mapper "/usr/bin/python mapper.py" \
    -reducer "/usr/bin/python reducer.py" \
    -input /home/punto2/data/input1_small.txt -output /home/punto2/data/output_hadoop_small

```

Caso de prueba completo con 5 reducers:
```
cd punto2/src/
```
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-$HADOOP_VERSION.jar -D mapreduce.job.reduces=5 \
    -files ./mapper.py,./reducer.py \
    -mapper "/usr/bin/python mapper.py" \
    -reducer "/usr/bin/python reducer.py" \
    -input /home/punto2/data/cite75_99.txt -output /home/punto2/data/output_hadoop_complete_5_reducers
```


Caso de prueba completo:
```
cd punto2/src/
```
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-$HADOOP_VERSION.jar\
    -files ./mapper.py,./reducer.py \
    -mapper "/usr/bin/python mapper.py" \
    -reducer "/usr/bin/python reducer.py" \
    -input /home/punto2/data/cite75_99.txt -output /home/punto2/data/output_hadoop_complete

```







