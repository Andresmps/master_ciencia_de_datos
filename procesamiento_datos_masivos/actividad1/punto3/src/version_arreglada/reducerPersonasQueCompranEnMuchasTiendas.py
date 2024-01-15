#!/usr/bin/python3

'''
Programa realizado por Jesus Moran
Este programa contiene un defecto que tienen que encontrar los alumnos
'''

import sys

subproblema = None
tiendas = 0

for claveValor in sys.stdin:
    cliente, tienda = claveValor.strip().split("\t", 1)
    tienda = int(tienda)

    if subproblema == None:
        subproblema = cliente

    if subproblema == cliente:
        tiendas += tienda
    else:
        if tiendas >= 3:
            print("%s" % (subproblema))

        subproblema = cliente
        tiendas = 0
        tiendas += tienda


if tiendas >= 3:
	print("%s" % (subproblema))
