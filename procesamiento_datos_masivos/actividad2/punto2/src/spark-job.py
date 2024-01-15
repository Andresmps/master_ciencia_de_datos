import sys
from pyspark.sql import SparkSession

# Inicializar SparkSession
spark = SparkSession\
    .builder\
    .appName('CategoriaDeVideosMenosVista')\
    .getOrCreate()

entrada = sys.argv[1]
salida = sys.argv[2]

# Cargar los datos de entrada en un RDD, excluyendo log.txt
datosEntrada = spark.sparkContext\
    .wholeTextFiles(entrada + "/*.txt")\
    .filter(lambda x: "log.txt" not in x[0])\
    .flatMap(lambda x: x[1].split('\n'))\
    .filter(lambda x: x.strip() != '')

# Procesar los datos
categorias_visitas = datosEntrada\
    .map(lambda linea: linea.split('\t'))\
    .filter(lambda x: len(x) > 6)\
    .map(lambda campos: (campos[3], int(campos[5])))\
    .reduceByKey(lambda x, y: x + y)

# Encontrar la categoría con menos visitas
categoria_menos_vista = categorias_visitas.reduce(
    lambda a, b: a if a[1] < b[1] else b)

# Guardar o mostrar el resultado
with open(salida, 'w') as archivo_salida:
    categoria, visitas = categoria_menos_vista
    archivo_salida.write(f"{categoria};{visitas}\n")
