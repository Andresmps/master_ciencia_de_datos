# Comandos para ejecutar los jobs punto 2
---

Caso de prueba del documento:
```
!rm -rf "actividad2/punto2/data/output/output.txt"
```
```
!$SPARK_HOME/bin/spark-submit \
    ./actividad2/punto2/src/spark-job.py \
    ./actividad2/punto2/data/input \
    ./actividad2/punto2/data/output/output.txt
```
```
!cat actividad2/punto2/data/output/output.txt
```

Caso de prueba usando el archivo 0302.zip de [Youtube-Data](https://netsg.cs.sfu.ca/youtubedata/):

```
!rm -rf "actividad2/punto2/data/output/output.txt"
```
```
!$SPARK_HOME/bin/spark-submit \
    ./actividad2/punto2/src/spark-job.py \
    ./actividad2/punto2/data/input \
    ./actividad2/punto2/data/output/output.txt
```
```
!cat actividad2/punto2/data/output/output.txt
```
