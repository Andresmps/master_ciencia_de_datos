# Comandos para ejecutar los jobs punto 1
---

Caso de prueba del documento:
```
!rm -rf "actividad2/punto1/data/output/"
```
La eliminación del output es para evitar problemas si se vuelve a ejecutar.
```
!$SPARK_HOME/bin/spark-submit \
    ./actividad2/punto1/src/spark-job.py \
    ./actividad2/punto1/data/input.txt \
    ./actividad2/punto1/data/output
```
Unificacion de las particiones resultantes.
```
!cat actividad2/punto1/data/output/part-* | sort > actividad2/punto1/data/output.txt
```
```
!cat actividad2/punto1/data/output.txt
```

