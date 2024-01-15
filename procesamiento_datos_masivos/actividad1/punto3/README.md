# Comandos para ejecutar los jobs punto 3
---

Caso de prueba reducido con problemas:
```
cd punto3/src/version_con_problemas
```
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-$HADOOP_VERSION.jar \
    -files ./mapperPersonasQueCompranEnMuchasTiendas.py,./combinerPersonasQueCompranEnMuchasTiendas.py,./reducerPersonasQueCompranEnMuchasTiendas.py \
    -mapper "/usr/bin/python mapperPersonasQueCompranEnMuchasTiendas.py" \
    -combiner "/usr/bin/python combinerPersonasQueCompranEnMuchasTiendas.py" \
    -reducer "/usr/bin/python reducerPersonasQueCompranEnMuchasTiendas.py" \
    -input /home/punto3/data/casoDePrueba_reducido.txt -output /home/punto3/data/output_hadoop_reducido
```

Caso de prueba reducido arreglado:
```
cd punto3/src/version_arreglado
```
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-$HADOOP_VERSION.jar \
    -files ./mapperPersonasQueCompranEnMuchasTiendas.py,./combinerPersonasQueCompranEnMuchasTiendas.py,./reducerPersonasQueCompranEnMuchasTiendas.py \
    -mapper "/usr/bin/python mapperPersonasQueCompranEnMuchasTiendas.py" \
    -combiner "/usr/bin/python combinerPersonasQueCompranEnMuchasTiendas.py" \
    -reducer "/usr/bin/python reducerPersonasQueCompranEnMuchasTiendas.py" \
    -input /home/punto3/data/casoDePrueba_reducido.txt -output /home/punto3/data/output_hadoop_reducido_arreglado
```


Caso de prueba completo con problemas:
```
cd punto3/src/version_con_problemas
```
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-$HADOOP_VERSION.jar \
    -files ./mapperPersonasQueCompranEnMuchasTiendas.py,./combinerPersonasQueCompranEnMuchasTiendas.py,./reducerPersonasQueCompranEnMuchasTiendas.py \
    -mapper "/usr/bin/python mapperPersonasQueCompranEnMuchasTiendas.py" \
    -combiner "/usr/bin/python combinerPersonasQueCompranEnMuchasTiendas.py" \
    -reducer "/usr/bin/python reducerPersonasQueCompranEnMuchasTiendas.py" \
    -input /home/punto3/data/casoDePrueba.txt -output /home/punto3/data/output_hadoop
```

Caso de prueba completo arreglado:
```
cd punto3/src/version_arreglado
```
```
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-$HADOOP_VERSION.jar \
    -files ./mapperPersonasQueCompranEnMuchasTiendas.py,./combinerPersonasQueCompranEnMuchasTiendas.py,./reducerPersonasQueCompranEnMuchasTiendas.py \
    -mapper "/usr/bin/python mapperPersonasQueCompranEnMuchasTiendas.py" \
    -combiner "/usr/bin/python combinerPersonasQueCompranEnMuchasTiendas.py" \
    -reducer "/usr/bin/python reducerPersonasQueCompranEnMuchasTiendas.py" \
    -input /home/punto3/data/casoDePrueba.txt -output /home/punto3/data/output_hadoop_arreglado
```
