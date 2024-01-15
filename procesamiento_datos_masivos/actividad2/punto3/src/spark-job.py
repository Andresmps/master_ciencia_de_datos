import sys
from pyspark.sql import SparkSession

# Inicializar SparkSession
spark = SparkSession\
    .builder\
    .appName('personaYMetodosDePago')\
    .getOrCreate()

entrada = sys.argv[1]
salida = sys.argv[2]
salida_mayor_1500 = '/comprasSinTDCMayorDe1500'
salida_menor_igual_1500 = '/comprasSinTDCMenoroIgualDe1500'

# Lee los datos
datosEntrada = spark.sparkContext.textFile(entrada)

# Incluye personas sin gastos de tarjeta de credito
personas = datosEntrada\
    .map(lambda linea: linea.split(';')[0])\
    .distinct()\
    .map(lambda persona: (persona, 0))

# Filtrar compras con tc
compras_sin_tc = datosEntrada\
    .map(lambda linea: linea.split(';'))\
    .filter(lambda x: x[1] != 'Tarjeta de crédito')\

# Tomar compras mayores a 1500
compras_mayores_1500 = compras_sin_tc\
    .filter(lambda x: int(x[2]) > 1500)\
    .map(lambda x: (x[0], 1))\
    .union(personas)\
    .reduceByKey(lambda x, y: x+y)

# Tomar compras menores o iguales a 1500
compras_menores_iguales_1500 = compras_sin_tc\
    .filter(lambda x: int(x[2]) <= 1500)\
    .map(lambda x: (x[0], 1))\
    .union(personas)\
    .reduceByKey(lambda x, y: x+y)

# Guardar las salidas
compras_mayores_1500.saveAsTextFile(salida + salida_mayor_1500)
compras_menores_iguales_1500.saveAsTextFile(salida + salida_menor_igual_1500)





