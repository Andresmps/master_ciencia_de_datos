# Comandos para ejecutar los jobs punto 1
---

Caso de prueba del documento:
```
!rm -rf "actividad2/punto3/data/output"
```
La eliminación del output es para evitar problemas si se vuelve a ejecutar.
```
!$SPARK_HOME/bin/spark-submit \
    ./actividad2/punto3/src/spark-job.py \
    ./actividad2/punto3/data/input.txt \
    ./actividad2/punto3/data/output
```
Unificacion de las particiones resultantes.
```
!cat actividad2/punto3/data/output/comprasSinTDCMayorDe1500/part-* | sort > actividad2/punto3/data/output/comprasSinTDCMayorDe1500_output.txt
!cat actividad2/punto3/data/output/comprasSinTDCMenoroIgualDe1500/part-* | sort > actividad2/punto3/data/output/comprasSinTDCMenoroIgualDe1500.txt
```
```
!cat actividad2/punto3/data/output/comprasSinTDCMayorDe1500_output.txt
!cat actividad2/punto3/data/output/comprasSinTDCMenoroIgualDe1500.txt
```

