# Importamos la líbreria necesaria
import datetime

from cassandra.cluster import Cluster

from creation_classes import \
    Ciudad, SoporteCine, Sala, Pelicula, Funcion, TipoBoleto, Reservacion, Usuario, Tarjeta,\
    FuncionTipoBoleto, FuncionReservacion, PeliculaReservacion, TipoBoletoReservacion,\
    ReservacionTarjeta

# Conexión a Cassandra
cluster = Cluster()
session = cluster.connect('camilomartinez')


# Funciones para insertar datos en la BBDD de Cassandra
def insertar_usuario():
    """
        Descripción: Función para pedir los datos de un usuario y almacenarlos en la base de datos
    """
    dni = input ("Dame el dni del usuario ")
    nombre = input("Dame el nombre del usuario ")
    tlfs = set()
    tlf = input("Dame los telefonos del cliente. Para detener la ejecución ingresa \".\".")

    while (tlf != ".".strip()):
        tlfs.add(tlf)
        tlf = input("Introduzca un teléfono. Para detener la ejecución ingresa \".\".")

    _usuario = Usuario(dni, nombre, tlfs)
    insertStatementPref = session.prepare(
        'INSERT INTO "Tabla7" ("usuario_tlf", "usuario_dni", "usuario_nombre", "usuario_tlfs") VALUES (?, ?, ?, ?)')

    # Insertamos los datos en la tabla para cada uno de los teléfonos - tlfs
    for telefono in tlfs:
        session.execute(insertStatementPref, [telefono, _usuario.DNI, _usuario.nombre, _usuario.tlfs])

    insertStatement2 = session.prepare(
        'INSERT INTO "SoporteUsuario" ("usuario_dni", "usuario_nombre", "usuario_tlfs") VALUES (?, ?, ?)')
    session.execute(insertStatement2, [_usuario.DNI, _usuario.nombre, _usuario.tlfs])

def insertar_pelicula():
    """
        Descripción: Función para pedir los datos de una película y almacenarlos en la base de datos
    """

    #Pedimos al usuario del programa los datos de la pelicula
    categoria = input ("Dame categoría de la película ")
    nombre = input ("Dame nombre de la película ")
    print("%d-%m-%Y %H:%M")
    fecha_hora = datetime.datetime.strptime(
        input("Dame fecha y hora de la función "), "%d-%m-%Y %H:%M")

    actores = set()
    actor = input("Dame actores de la película. Para detener la ejecución ingresa \".\".")

    while (actor != "."):
        actores.add(actor)
        actor = input("Introduzca un actor. Para detener la ejecución ingresa \".\".")

    pelicula = extraerDatosPelicula(nombre)
    _pelicula = Pelicula(nombre, categoria, actores)

    # Si la película no está en la base de datos, la insertamos
    if (pelicula is None):
        # Inserción de datos Tabla1
        insertStatement = session.prepare (
            'INSERT INTO "Tabla1" (pelicula_categoria, pelicula_nombre, funcion_fecha_hora,'
            'pelicula_actores) VALUES (?, ?, ?, ?, ?, ?)')

        session.execute (
            insertStatement, [_pelicula.categoria, _pelicula.IdNombrePelicula, fecha_hora, _pelicula.actores])

        # Inserción de datos Tabla6
        insertStatement2 = session.prepare(
            'INSERT INTO "Tabla6" (pelicula_categoria, pelicula_nombre, pelicula_actores) VALUES (?, ?, ?, ?)')
        session.execute(insertStatement2, [_pelicula.categoria, _pelicula.IdNombrePelicula, _pelicula.actores])

        # Inserción de datos SoportePelicula
        insertStatement3 = session.prepare(
            'INSERT INTO "SoportePelicula" (pelicula_nombre, pelicula_categoria, pelicula_actores) VALUES (?, ?, ?)')
        session.execute(insertStatement3, [_pelicula.IdNombrePelicula, _pelicula.categoria, _pelicula.actores])

def insertar_cine():
    """
        Descripción: Función para pedir los datos de un cine y almacenarlos en la base de datos
    """
    id = input("Dame el ID del cine ")
    nombre = input("Dame nombre del cine ")
    ubicacion = input("Dame ubicación del cine ")
    ciudad_nombre = input("Dame nombre de la ciudad del cine ")
    cine = extraerDatosCine(nombre, ciudad_nombre)
    _cine = SoporteCine(id, nombre, ubicacion, ciudad_nombre)

    # Si el cine no está en la base de datos, lo insertamos
    if (cine is None):
        # Inserción de datos SoporteCine
        insertStatement = session.prepare(
            'INSERT INTO "SoporteCine" (cine_id, cine_nombre, cine_ubicacion) VALUES (?, ?, ?)')

        session.execute(insertStatement, [_cine.IdCine, _cine.nombre, _cine.ubicacion])

def insertar_reserva_compra():
    """
        Descripción: Función para pedir los datos de un usuario, reserva y compra y almacenarlos en la base de datos
    """
    usuario_dni = input("Dame el DNI del usuario ")
    reservacion_nro = input("Dame el número de reservación ")
    tipo_boleto_nombre = input("Dame el nombre del tipo de boleto ")

    usuario = extraerDatosUsuario(usuario_dni)

    # Si el usuario no está en la base de datos, lo insertamos
    if (usuario is None):
        print("El usuario no está en la base de datos. Por favor, inserte el usuario primero.")
    else:
        # Inserción de datos Tabla2
        insertStatement = session.prepare(
            'INSERT INTO "Tabla2" (usuario_dni, reservacion_nro, tipo_boleto_nombre) VALUES (?, ?, ?, ?, ?)')

        session.execute(
            insertStatement, [usuario_dni, reservacion_nro, tipo_boleto_nombre])

def insertar_cine_sala():
    """
        Descripción: Función para pedir los datos de un cine, sala y almacenarlos en la base de datos
    """

    cine_id = input("Dame el id del cine ")
    ciudad_cine = input("Dame la ciudad del cine ")
    sala_nro = int(input("Dame el número de la sala "))
    cine = extraerDatosCine(cine_id, ciudad_cine)
    _sala = Sala(sala_nro, cine_id)

    # Si el cine no está en la base de datos, lo insertamos
    if (cine is None):
        # Inserción de datos SoporteCine si el cine no está
        cine_nombre = input("Dame el nombre del cine ")
        cine_ubicacion = input("Dame la ubicación del cine ")

        insertStatement2 = session.prepare(
            'INSERT INTO "SoporteCine" (cine_id, cine_nombre, cine_ubicacion) VALUES (?, ?, ?)')
        session.execute(insertStatement2, [cine_id, cine_nombre, cine_ubicacion])

    insertStatement = session.prepare(
        'INSERT INTO "Tabla3" (cine_nombre, sala_nro) VALUES (?, ?, ?)')
    session.execute(insertStatement, [cine_nombre, sala_nro])

def insertar_tarjeta_reserva():
    """
        Descripción: Función para pedir los datos de una tarjeta y reserva y almacenarlos en la base de datos
    """
    tarjeta_nro = int(input("Dame el número de la tarjeta "))
    tarjeta_banco = input("Dame el banco de la tarjeta ")
    tarjeta_fecha = input("Dame la fecha de vencimiento de la tarjeta ")
    reservacion_nro = int(input("Dame el número de reservación "))
    reservacion_confirmado = bool(input("Indica si se ha confirmado la reserva (1, 0) "))

    reserva = extraerDatosReserva(reservacion_nro)
    tarjeta = extraerDatosTarjeta(tarjeta_nro)

    if (reserva is None and tarjeta==None):
        insertStatement = session.prepare(
            'INSERT INTO "SoporteReservacion" (reservacion_nro, reservacion_confirmado) VALUES (?, ?)')
        session.execute(insertStatement, [reservacion_nro, reservacion_confirmado])
        insertStatement2 = session.prepare(
            'INSERT INTO "Tabla5" (tarjeta_banco, tarjeta_nro, reservacion_nro, reservacion_confirmado) VALUES (?, ?, ?, ?)')
        session.execute(insertStatement2, [tarjeta_banco, tarjeta_nro, reservacion_nro, reservacion_confirmado])
        insertStatement3 = session.prepare(
            'INSERT INTO "SoporteTarjeta" (tarjeta_nro, tarjeta_banco, tarjeta_fecha) VALUES (?, ?, ?)')
        session.execute(insertStatement3, [tarjeta_nro, tarjeta_banco, tarjeta_fecha])
    elif (reserva != None and tarjeta==None):
        insertStatement2 = session.prepare(
            'INSERT INTO "Tabla5" (tarjeta_banco, tarjeta_nro, reservacion_nro, reservacion_confirmado) VALUES (?, ?, ?, ?)')
        session.execute(insertStatement2, [tarjeta_banco, tarjeta_nro, reserva.IdNroReservacion, reserva.confirmado])
        insertStatement3 = session.prepare(
            'INSERT INTO "SoporteTarjeta" (tarjeta_nro, tarjeta_banco, tarjeta_fecha) VALUES (?, ?, ?)')
        session.execute(insertStatement3, [tarjeta_nro, tarjeta_banco, tarjeta_fecha])
    elif (reserva is None and tarjeta!=None):
        insertStatement = session.prepare(
            'INSERT INTO "SoporteReservacion" (reservacion_nro, reservacion_confirmado) VALUES (?, ?)')
        session.execute(insertStatement, [reservacion_nro, reservacion_confirmado])
        insertStatement2 = session.prepare(
            'INSERT INTO "Tabla5" (tarjeta_banco, tarjeta_nro, reservacion_nro, reservacion_confirmado) VALUES (?, ?, ?, ?)')
        session.execute(insertStatement2, [tarjeta.banco, tarjeta.IdNro, reservacion_nro, reservacion_confirmado])
    else:
        insertStatement = session.prepare(
            'INSERT INTO "Tabla5" (tarjeta_banco, tarjeta_nro, reservacion_nro, reservacion_confirmado) VALUES (?, ?, ?, ?)')
        session.execute(insertStatement, [tarjeta.banco, tarjeta.IdNro, reserva.IdNroReservacion, reserva.confirmado])

def extraerDatosPelicula(pelicula_nombre):
    """
        Descripción: Función para extraer los datos de la película dado su nombre
    """
    select = session.prepare(
        'SELECT * FROM "SoportePelicula" WHERE pelicula_nombre = ?')
    filas = session.execute (select, [pelicula_nombre,])

    for fila in filas:
        _pelicula = Pelicula(
            fila.pelicula_nombre, fila.pelicula_categoria,
            fila.pelicula_actores) #creamos instancia del cliente

    return _pelicula

def extraerDatosCine(cine_id, ciudad_nombre):
    """
        Descripción: Función para extraer los datos del cine dado su id
    """
    select = session.prepare ('SELECT * FROM "SoporteCine" WHERE cine_id = ?')
    filas = session.execute (select, [cine_id,])
    for fila in filas:
        _cine = SoporteCine(
            fila.cine_id, fila.cine_nombre, fila.cine_ubicacion, ciudad_nombre)

    return _cine

def extraerDatosUsuario(usuario_dni):
    """
        Descripción: Función para extraer los datos del usuario dado su dni
    """
    select = session.prepare(
        'SELECT * FROM "SoporteUsuario" WHERE usuario_dni = ?')
    filas = session.execute(select, [
        usuario_dni, ])

    for fila in filas:
        _usuario = Usuario(
            fila.usuario_dni, fila.usuario_nombre, fila.usuario_tlfs)
    return _usuario

def extraerDatosReserva(nro):
    """
        Descripción: Función para extraer los datos de la reserva dado su nro
    """
    select = session.prepare (
        'SELECT * FROM "SoporteReservacion" WHERE reservacion_nro = ?')
    filas = session.execute(select, [nro,])

    for fila in filas:
        _reserva = Reservacion(fila.reserva_nro, fila.reserva_confirmado, "")
    return _reserva

def extraerDatosTarjeta(nro):
    """
        Descripción: Función para extraer los datos de la tarjeta dado su nro
    """
    select = session.prepare ('SELECT * FROM "SoporteTarjeta" WHERE tarjeta_nro = ?')
    filas = session.execute (select, [nro,])
    for fila in filas:
        _tarjeta = Tarjeta(
            fila.tarjeta_nro, fila.tarjeta_fecha, fila.tarjeta_banco)
    return _tarjeta


def extraerDatosTabla5(banco):
    """
        Descripción: Función para extraer los datos de la tabla 5 dado el banco
    """
    select = session.prepare ('SELECT * FROM "Tabla5" WHERE tarjeta_banco = ?')
    filas = session.execute (select, [banco,])
    t5 = []
    for fila in filas:
        t = Tarjeta(fila.tarjeta_nro, "", fila.tarjeta_banco)
        r = Reservacion(fila.reservacion_nro, fila.reservacion_confirmado, "")
        t5.append({
            'tarjeta_nro':t.IdNro, 'tarjeta_banco':t.banco,
            'reservacion_nro': r.IdNroReservacion, 'reservacion_confirmado':r.confirmado})
    return t5

def extraerDatosTabla1(pelicula):
    """
        Descripción: Función para extraer los datos de la tabla 1 dado el nombre de la película
    """
    categoria = extraerDatosPelicula(pelicula).categoria
    select = session.prepare(
        'SELECT * FROM "Tabla1" WHERE pelicula_categoria = ? AND pelicula_nombre = ?')
    filas = session.execute(select, [
        categoria, pelicula, ])

    t1 = []
    for fila in filas:
        p = Pelicula(fila.pelicula_nombre, fila.pelicula_categoria, fila.pelicula_actores)
        t1.append({
            'pelicula_categoria':p.categoria, 'pelicula_nombre':p.IdNombrePelicula,
            'funcion_fecha_hora':fila.funcion_fecha_hora, 'pelicula_actores':p.actores,
            'sala_nro':fila.sala_nro, 'sala_capacidad':fila.sala_capacidad})
    return t1


numero = -1
#Sigue pidiendo operaciones hasta que se introduzca 0
while (numero != 0):
    print ("Introduzca un número para ejecutar una de las siguientes operaciones:")
    print ("1. Insertar un usuario")
    print ("2. Insertar una película")
    print ("3. Insertar cine")
    print ("4. Insertar relación entre usuario, reservación y tipo_boleto")
    print ("5. Insertar relación entre cine y sala")
    print ("0. Cerrar aplicación")

    numero = int (input()) #Pedimos numero al usuario
    if (numero == 1):
        insertar_usuario()
    elif (numero == 2):
        insertar_pelicula()
    elif (numero == 3):
        insertar_cine()
    elif (numero == 4):
        insertar_reserva_compra()
    elif (numero == 5):
        insertar_cine_sala()
    else:
        print ("Número incorrecto")

# Cerramos la sesión

session.shutdown()

