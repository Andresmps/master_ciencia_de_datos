# Comandos para ejecutar los jobs punto 1
---

Caso de prueba reducido:
```
cd punto1/src/
```
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-$HADOOP_VERSION.jar \
    -files ./mapper.py,./combiner.py,./reducer.py \
    -mapper "/usr/bin/python mapper.py" \
    -combiner "/usr/bin/python combiner.py" \
    -reducer "/usr/bin/python reducer.py" \
    -input /home/punto1/data/input1.txt -output /home/punto1/data/output_hadoop

```
