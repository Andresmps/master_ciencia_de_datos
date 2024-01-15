#!/usr/bin/python3

import sys
from pyspark.sql import SparkSession

# Inicia la aplicación
spark = SparkSession\
    .builder\
    .appName('personaGastosConTarjetaCredito')\
    .getOrCreate()

entrada = sys.argv[1]
salida = sys.argv[2]

# Lee los datos
datosEntrada = spark.sparkContext.textFile(entrada)

# Incluye personas sin gastos de tarjeta de credito
personas = datosEntrada\
    .map(lambda linea: linea.split(';')[0])\
    .distinct()\
    .map(lambda persona: f"{persona};Tarjeta de crédito;0")

datosEntrada = datosEntrada\
    .union(personas)\

# Agrega los datos
gastosConTDC = datosEntrada\
    .map(lambda linea: linea.split(';'))\
    .filter(lambda x: x[1] == 'Tarjeta de crédito')\
    .map(lambda x: (x[0], float(x[2])))\
    .reduceByKey(lambda x, y: x + y)\
    .map(lambda x: f'{x[0]};{x[1]}')

# Guardar la salida
gastosConTDC.saveAsTextFile(salida)
