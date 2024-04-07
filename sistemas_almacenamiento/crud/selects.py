import logging

from dataclasses import dataclass
from datetime import datetime

from .clases_tablas import Usuario, Pelicula, Ciudad, Cine, Reservacion, TipoBoleto,\
    CiudadCine, CineSala, Tarjeta, PeliculaFuncion, Sala
from .utils import TipoOperacion, queryStringTemplates, Logging

logging.basicConfig(
    format=Logging.MSG_FORMAT.value,
    datefmt=Logging.DATETIME_FORMAT.value, level=logging.INFO,
)

logger = logging.getLogger(Logging.SELECTS_LOGGER.value)

@dataclass
class Selects:
    session: object

    def mostrarDatosUsuario(self):
        """
            Descripción: Función para mostrar los datos de los usuarios
        """
        query_select_usuario = queryStringTemplates(
            tabla='SoporteUsuario', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de los usuarios
        select = self.session.prepare(query_select_usuario)
        filas = self.session.execute(select)
        usuarios = []

        for fila in filas:
            _usuario = Usuario(
                fila.usuario_dni, fila.usuario_nombre, fila.usuario_tlfs)
            usuarios.append(_usuario)
            logger.info(f"\n\tUsuario encontrado - {_usuario}\n")
        return usuarios

    def mostrarDatosPelicula(self):
        """
            Descripción: Función para mostrar los datos de las películas
        """
        query_select_pelicula = queryStringTemplates(
            tabla='SoportePelicula', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de las películas
        select = self.session.prepare(query_select_pelicula)
        filas = self.session.execute(select)

        for fila in filas:
            _pelicula = Pelicula(
                fila.pelicula_nombre, fila.pelicula_categoria, fila.pelicula_actores)
            logger.info(f"\n\tPelicula encontrada - {_pelicula}\n")

    def mostrarDatosCiudad(self):
        """
            Descripción: Función para mostrar los datos de las ciudades
        """
        query_select_ciudad = queryStringTemplates(
            tabla='SoporteCiudad', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de las ciudades
        select = self.session.prepare(query_select_ciudad)
        filas = self.session.execute(select)
        ciudades = []

        for fila in filas:
            _ciudad = Ciudad(
                fila.ciudad_nombre, fila.ciudad_provincia, fila.ciudad_comunidad_autonoma)
            ciudades.append(_ciudad)
            logger.info(f"\n\tCiudad encontrada - {_ciudad}\n")

        return ciudades

    def mostrarDatosCine(self):
        """
            Descripción: Función para mostrar los datos de los cines
        """
        query_select_cine = queryStringTemplates(
            tabla='SoporteCine', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de los cines
        select = self.session.prepare(query_select_cine)
        filas = self.session.execute(select)
        cines = []

        for fila in filas:
            _cine = Cine(fila.cine_id, fila.cine_nombre, fila.cine_ubicacion)
            cines.append(_cine)
            logger.info(f"\n\tCine encontrado - {_cine}\n")
        return cines

    def mostrarDatosSala(self):
        """
            Descripción: Función para mostrar los datos de las salas
        """
        query_select_sala = queryStringTemplates(
            tabla='SoporteSala', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de las salas
        select = self.session.prepare(query_select_sala)
        filas = self.session.execute(select)
        salas  = []

        for fila in filas:
            _sala = Sala(
                fila.sala_nro, fila.capacidad)
            salas.append(_sala)
            logger.info(f"\n\tSala encontrada - {_sala}\n")
        return salas

    def mostrarDatosTarjeta(self):
        """
            Descripción: Función para mostrar los datos de las tarjetas
        """
        query_select_tarjeta = queryStringTemplates(
            tabla='SoporteTarjeta', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de las tarjetas
        select = self.session.prepare(query_select_tarjeta)
        filas = self.session.execute(select)
        tarjetas = []

        for fila in filas:
            _tarjeta = Tarjeta(
                fila.tarjeta_nro, fila.tarjeta_fecha, fila.tarjeta_banco)
            tarjetas.append(_tarjeta)
            logger.info(f"\n\tTarjeta encontrada - {_tarjeta}\n")
        return tarjetas

    def mostrarDatosTipoBoleto(self):
        """
            Descripción: Función para mostrar los datos de los tipos de boleto
        """
        query_select_tipo_boleto = queryStringTemplates(
            tabla='SoporteTipoBoleto', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de los tipos de boleto
        select = self.session.prepare(query_select_tipo_boleto)
        filas = self.session.execute(select)
        tipo_boletos = []

        for fila in filas:
            _tipo_boleto = TipoBoleto(
                fila.tipo_boleto, fila.descuento)
            tipo_boletos.append(_tipo_boleto)
            logger.info(f"\n\tTipo de boleto encontrado - {_tipo_boleto}\n")
        return tipo_boletos

    def mostrarDatosPeliculaFuncion(self):
        """
            Descripción: Función para mostrar los datos de las funciones de las películas
        """
        query_select_funcion = queryStringTemplates(
            tabla='PeliculaFuncion', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de las funciones de las películas
        select = self.session.prepare(query_select_funcion)
        filas = self.session.execute(select)
        funciones = []

        for fila in filas:
            _funcion = PeliculaFuncion(
                fila.funcion_fecha_hora, fila.pelicula_nombre, fila.porcentaje_ocupacion)
            funciones.append(_funcion)
            logger.info(f"\n\tFunción encontrada - {_funcion}\n")
        return funciones

    def mostrarDatosReservacion(self):
        """
            Descripción: Función para mostrar los datos de las reservaciones
        """
        query_select_reservacion = queryStringTemplates(
            tabla='SoporteReservacion', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de las reservaciones
        select = self.session.prepare(query_select_reservacion)
        filas = self.session.execute(select)
        reservaciones = []

        for fila in filas:
            _reservacion = Reservacion(
                fila.reservacion_nro, fila.reservacion_confirmado,
                fila.funcion_fecha_hora, fila.pelicula_nombre)
            reservaciones.append(_reservacion)
            logger.info(f"\n\tReservación encontrada - {_reservacion}\n")

        return reservaciones

    def selectDatosUsuario(self, usuario_dni: str=None):
        """
            Descripción: Función para extraer los datos del usuario dado su dni
        """

        if usuario_dni is None:
            usuario_dni = input("Ingresa el DNI del usuario: ")

        _usuario = None
        query_select_usuario = queryStringTemplates(
            tabla='SoporteUsuario', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['usuario_dni'])

        # Consulta para extraer los datos del usuario
        select = self.session.prepare(query_select_usuario)
        filas = self.session.execute(select, [usuario_dni])

        if not filas:
            # # # logger.info(f"No se encontró el usuario con el DNI={usuario_dni}\n")
            return _usuario

        # Como usuario_dni es clave primaria, solo se espera un resultado
        for fila in filas:
            _usuario = Usuario(
                fila.usuario_dni, fila.usuario_nombre, fila.usuario_tlfs)
            logger.info(f"\n\tUsuario encontrado - {_usuario}\n")

        return _usuario

    def selectDatosPelicula(self, pelicula_nombre: str=None):
        """
            Descripción: Función para extraer los datos de la película dado su nombre
        """

        if pelicula_nombre is None:
            pelicula_nombre = input("Ingresa el nombre de la película: ")

        _pelicula = None
        query_select_pelicula = queryStringTemplates(
            tabla='SoportePelicula', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['pelicula_nombre'])

        # Consulta para extraer los datos de la película
        select = self.session.prepare(query_select_pelicula)
        filas = self.session.execute(select, [pelicula_nombre])

        if not filas:
            # # # logger.info(f"No se encontró la película con el nombre={pelicula_nombre}\n")
            return _pelicula

        # Como pelicula_nombre es clave primaria, solo se espera un resultado
        for fila in filas:
            _pelicula = Pelicula(
                fila.pelicula_nombre, fila.pelicula_categoria, fila.pelicula_actores)
            logger.info(f"\n\tPelicula encontrada - {_pelicula}\n")

        return _pelicula

    def selectDatosCiudad(self, ciudad_nombre: str=None):
        """
            Descripción: Función para extraer los datos de la ciudad dado su nombre
        """

        if ciudad_nombre is None:
            ciudad_nombre = input("Ingresa el nombre de la ciudad: ")

        _ciudad = None
        query_select_ciudad = queryStringTemplates(
            tabla='SoporteCiudad', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['ciudad_nombre'])

        # Consulta para extraer los datos de la ciudad
        select = self.session.prepare(query_select_ciudad)
        filas = self.session.execute(select, [ciudad_nombre])

        if not filas:
            # # # logger.info(f"No se encontró la ciudad con el nombre={ciudad_nombre}\n")
            return _ciudad

        # Como ciudad_nombre es clave primaria, solo se espera un resultado
        for fila in filas:
            _ciudad = Ciudad(
                fila.ciudad_nombre, fila.ciudad_provincia, fila.ciudad_comunidad_autonoma)
            logger.info(f"\n\tCiudad encontrada - {_ciudad}\n")

        return _ciudad

    def selectDatosCine(self, cine_id: str=None):
        """
            Descripción: Función para extraer los datos del cine dado su id
        """
        if cine_id is None:
            cine_id = input("Ingresa el id del cine: ")

        _cine = None
        query_select_cine = queryStringTemplates(
            tabla='SoporteCine', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['cine_id'])

        # Consulta para extraer los datos del cine
        select = self.session.prepare(query_select_cine)
        filas = self.session.execute(select, [cine_id])

        if not filas:
            # # # logger.info(f"No se encontró el cine con el id={cine_id}\n")
            return _cine

        # Como cine_id es clave primaria, solo se espera un resultado
        for fila in filas:
            _cine = Cine(fila.cine_id, fila.cine_nombre, fila.cine_ubicacion)
            logger.info(f"\n\tCine encontrado - {_cine}\n")

        return _cine

    def selectDatosSala(self, sala_nro: int=None):
        """
            Descripción: Función para extraer los datos de la sala dado su número
        """

        if sala_nro is None:
            sala_nro = int(input("Ingresa el número de la sala: "))

        _sala = None
        query_select_sala = queryStringTemplates(
            tabla='SoporteSala', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['sala_nro'])

        # Consulta para extraer los datos de la sala
        select = self.session.prepare(query_select_sala)
        filas = self.session.execute(select, [sala_nro])

        if not filas:
            # # # logger.info(f"No se encontró la sala con el número={sala_nro}\n")
            return _sala

        # Como sala_nro es clave primaria, solo se espera un resultado
        for fila in filas:
            _sala = CineSala(
                fila.sala_nro, fila.capacidad)
            logger.info(f"\n\tSala encontrada - {_sala}\n")

        return _sala

    def selectDatosReservacion(self, nro_reservacion: str=None):
        """
            Descripción: Función para extraer los datos de la reservación dado su número
        """

        if nro_reservacion is None:
            nro_reservacion = input("Ingresa el número de la reservación: ")

        _reservacion = None
        query_select_reservacion = queryStringTemplates(
            tabla='SoporteReservacion', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['reservacion_nro'])

        # Consulta para extraer los datos de la reservación
        select = self.session.prepare(query_select_reservacion)
        filas = self.session.execute(select, [nro_reservacion])

        if not filas:
            # # # logger.info(f"No se encontró la reservación con el número={nro_reservacion}\n")
            return _reservacion

        # Como reservacion_nro es clave primaria, solo se espera un resultado
        for fila in filas:
            _reservacion = Reservacion(
                fila.reservacion_nro, fila.reservacion_confirmado, fila.funcion_fecha_hora, fila.pelicula_nombre)
            logger.info(f"\n\tReservación encontrada - {_reservacion}\n")

        return _reservacion

    def selectDatosTipoBoleto(self, nombre_tipo_boleto: str=None):
        """
            Descripción: Función para extraer los datos del tipo de boleto dado su nombre
        """
        if nombre_tipo_boleto is None:
            nombre_tipo_boleto = input("Ingresa el nombre del tipo de boleto: ")

        _tipo_boleto = None
        query_select_tipo_boleto = queryStringTemplates(
            tabla='SoporteTipoBoleto', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['tipo_boleto'])

        # Consulta para extraer los datos del tipo de boleto
        select = self.session.prepare(query_select_tipo_boleto)
        filas = self.session.execute(select, [nombre_tipo_boleto])

        if not filas:
            # # # logger.info(f"No se encontró el tipo de boleto con el nombre={nombre_tipo_boleto}\n")
            return _tipo_boleto

        # Como tipo_boleto es clave primaria, solo se espera un resultado
        for fila in filas:
            _tipo_boleto = TipoBoleto(
                fila.tipo_boleto, fila.descuento)
            logger.info(f"\n\tTipo de boleto encontrado - {_tipo_boleto}\n")

        return _tipo_boleto

    def selectDatosPeliculaFuncion(self, fecha_hora: datetime = None):
        """
            Descripción: Función para extraer los datos de la función dado su fecha y hora
        """
        _funcion = None
        if fecha_hora is None:
            fecha_hora = input("Ingresa la fecha y hora de la función (YYYYMMDD_HHMM): ")
            fecha_hora = datetime.strptime(fecha_hora, '%Y%m%d_%H%M')

        query_select_funcion = queryStringTemplates(
            tabla='PeliculaFuncion', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['funcion_fecha_hora'])

        # Consulta para extraer los datos de la función
        select = self.session.prepare(query_select_funcion)
        filas = self.session.execute(select, [fecha_hora])

        if not filas:
            # # # logger.info(f"No se encontró la función con la fecha y hora={fecha_hora}\n")
            return _funcion

        # Como funcion_fecha_hora es clave primaria, solo se espera un resultado
        for fila in filas:
            _funcion = PeliculaFuncion(
                fila.funcion_fecha_hora, fila.pelicula_nombre, fila.porcentaje_ocupacion)
            logger.info(f"\n\tFunción encontrada - {_funcion}\n")

        return _funcion

    def selectDatosCiudadCine(self, cine_id: str=None):
        """
            Descripción: Función para extraer los datos de la ciudad dado el id del cine
        """
        _ciudad_cine = None
        if cine_id is None:
            cine_id = input("Ingresa el id del cine: ")

        query_select_ciudad = queryStringTemplates(
            tabla='CiudadCine', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['cine_id'])

        # Consulta para extraer los datos de la ciudad
        select = self.session.prepare(query_select_ciudad)
        filas = self.session.execute(select, [cine_id])

        if not filas:
            # # logger.info(f"No se encontró la ciudad con el id del cine={cine_id}\n")
            return _ciudad_cine

        # Como ciudad_id es clave primaria, solo se espera un resultado
        for fila in filas:
            _ciudad_cine = CiudadCine(
                fila.cine_id, fila.ciudad_nombre)
            logger.info(f"\n\tCiudad encontrada - {_ciudad_cine}\n")

        return _ciudad_cine

    def selectDatosCineSala(self, sala_nro:int=None):
        """
            Descripción: Función para extraer los datos de la sala dado su número
        """
        _sala = None
        if sala_nro is None:
            sala_nro = int(input("Ingresa el número de la sala: "))

        query_select_sala = queryStringTemplates(
            tabla='CineSala', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['sala_nro'])

        # Consulta para extraer los datos de la sala
        select = self.session.prepare(query_select_sala)
        filas = self.session.execute(select, [sala_nro])

        if not filas:
            # # logger.info(f"No se encontró la sala con el número={sala_nro}\n")
            return _sala

        # Como sala_nro es clave primaria, solo se espera un resultado
        for fila in filas:
            _sala = CineSala(
                fila.cine_id, fila.sala_nro)
            logger.info(
                f"\n\tSala encontrada - {_sala}\n")

        return _sala

    def selectDatosTarjeta(self, tarjeta_nro:int=None):
        """
            Descripción: Función para extraer los datos de la tarjeta dado su número
        """
        _tarjeta = None
        if tarjeta_nro is None:
            tarjeta_nro = int(input("Ingresa el número de la tarjeta: "))

        query_select_tarjeta = queryStringTemplates(
            tabla='SoporteTarjeta', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['tarjeta_nro'])

        # Consulta para extraer los datos de la tarjeta
        select = self.session.prepare(query_select_tarjeta)
        filas = self.session.execute(select, [tarjeta_nro])

        if not filas:
            # # logger.info(f"No se encontró la tarjeta con el número={tarjeta_nro}\n")
            return _tarjeta

        # Como tarjeta_nro es clave primaria, solo se espera un resultado
        for fila in filas:
            _tarjeta = Tarjeta(
                fila.tarjeta_nro, fila.tarjeta_fecha, fila.tarjeta_banco)
            logger.info(
                f"\n\tTarjeta encontrada - {_tarjeta}\n")

        return _tarjeta

    def mostrarDatosTabla1(self):
        """
            Descripción: Función para mostrar los datos de la tabla1
        """
        query_select = queryStringTemplates(
            tabla='Tabla1', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de la tabla1
        select = self.session.prepare(query_select)
        filas = self.session.execute(select)
        datos = []

        for fila in filas:
            logger.info(f"\n\tFila encontrada - {fila}\n")
            datos.append(fila)

        return datos

    def mostrarDatosTabla2(self):
        """
            Descripción: Función para mostrar los datos de la tabla2
        """
        query_select = queryStringTemplates(
            tabla='Tabla2', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de la tabla2
        select = self.session.prepare(query_select)
        filas = self.session.execute(select)

        for fila in filas:
            logger.info(f"\n\tFila encontrada - {fila}\n")

    def mostrarDatosTabla3(self):
        """
            Descripción: Función para mostrar los datos de la tabla3
        """
        query_select = queryStringTemplates(
            tabla='Tabla3', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de la tabla3
        select = self.session.prepare(query_select)
        filas = self.session.execute(select)

        for fila in filas:
            logger.info(f"\n\tFila encontrada - {fila}\n")

    def mostrarDatosTabla4(self):
        """
            Descripción: Función para mostrar los datos de la tabla4
        """
        query_select = queryStringTemplates(
            tabla='Tabla4', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de la tabla4
        select = self.session.prepare(query_select)
        filas = self.session.execute(select)

        for fila in filas:
            logger.info(f"\n\tFila encontrada - {fila}\n")

    def mostrarDatosTabla5(self):
        """
            Descripción: Función para mostrar los datos de la tabla5
        """
        query_select = queryStringTemplates(
            tabla='Tabla5', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de la tabla5
        select = self.session.prepare(query_select)
        filas = self.session.execute(select)
        datos = []

        for fila in filas:
            logger.info(f"\n\tFila encontrada - {fila}\n")
            datos.append(fila)

        return datos

    def mostrarDatosTabla6(self):
        """
            Descripción: Función para mostrar los datos de la tabla6
        """
        query_select = queryStringTemplates(
            tabla='Tabla6', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de la tabla6
        select = self.session.prepare(query_select)
        filas = self.session.execute(select)

        for fila in filas:
            logger.info(f"\n\tFila encontrada - {fila}\n")

    def mostrarDatosTabla7(self):
        """
            Descripción: Función para mostrar los datos de la tabla7
        """
        query_select = queryStringTemplates(
            tabla='Tabla7', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de la tabla7
        select = self.session.prepare(query_select)
        filas = self.session.execute(select)

        for fila in filas:
            logger.info(f"\n\tFila encontrada - {fila}\n")

    def mostrarDatosTabla8(self):
        """
            Descripción: Función para mostrar los datos de la tabla8
        """
        query_select = queryStringTemplates(
            tabla='Tabla8', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True)

        # Consulta para extraer los datos de la tabla8
        select = self.session.prepare(query_select)
        filas = self.session.execute(select)

        for fila in filas:
            logger.info(f"\n\tFila encontrada - {fila}\n")

    def selectDatosTabla1(self, pelicula_categoria: str=None):
        """
            Descripción: Función para extraer los datos de la tabla1 dado la categoría y nombre de la película
        """

        if pelicula_categoria is None:
            pelicula_categoria = input("Ingresa la categoría de la película: ")

        query_select = queryStringTemplates(
            tabla='Tabla1', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['pelicula_categoria'])

        # Consulta para extraer los datos de la tabla1
        select = self.session.prepare(query_select)
        filas = self.session.execute(select, [pelicula_categoria])
        df_rows = []

        for fila in filas:
            df_rows.append({
                'pelicula_categoria': fila.pelicula_categoria,
                'pelicula_nombre': fila.pelicula_nombre,
                'pelicula_actores': list(fila.pelicula_actores)
            })
        return df_rows

    def selectDatosTabla2(self, usuario_dni: str=None):
        """
            Descripción: Función para extraer los datos de la tabla2 dado el dni del usuario
        """

        if usuario_dni is None:
            usuario_dni = input("Ingresa el DNI del usuario: ")

        query_select = queryStringTemplates(
            tabla='Tabla2', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['usuario_dni'])

        # Consulta para extraer los datos de la tabla2
        select = self.session.prepare(query_select)
        filas = self.session.execute(select, [usuario_dni])
        df_rows = []

        for fila in filas:
            df_rows.append({
                'usuario_dni': fila.usuario_dni,
                'reservacion_nro': fila.reservacion_nro,
                'tipo_boleto': fila.tipo_boleto_nombre
            })
        return df_rows

    def selectDatosTabla3(self, cine_nombre: str=None):
        """
            Descripción: Función para extraer los datos de la tabla3 dado el nombre del cine
        """

        if cine_nombre is None:
            cine_nombre = input("Ingresa el nombre del cine: ")

        query_select = queryStringTemplates(
            tabla='Tabla3', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['cine_nombre'])

        # Consulta para extraer los datos de la tabla3
        select = self.session.prepare(query_select)
        filas = self.session.execute(select, [cine_nombre])
        df_rows = []

        for fila in filas:
            df_rows.append({
                'cine_nombre': fila.cine_nombre,
                'sala_nro': fila.sala_nro
            })
        return df_rows

    def selectDatosTabla4(self, usuario_dni: str=None):
        """
            Descripción: Función para extraer los datos de la tabla4 dado el dni del usuario
        """

        if usuario_dni is None:
            usuario_dni = input("Ingresa el DNI del usuario: ")

        query_select = queryStringTemplates(
            tabla='Tabla4', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['usuario_dni'])

        # Consulta para extraer los datos de la tabla4
        select = self.session.prepare(query_select)
        filas = self.session.execute(select, [usuario_dni])
        df_rows = []

        for fila in filas:
            df_rows.append({
                'usuario_dni': fila.usuario_dni,
                'conteo_reservaciones': fila.reservacion_nro
            })
        return df_rows

    def selectDatosTabla5(self, tarjeta_banco: str=None):
        """
            Descripción: Función para extraer los datos de la tabla5 dado el banco de la tarjeta
        """

        if tarjeta_banco is None:
            tarjeta_banco = input("Ingresa el banco de la tarjeta: ")

        query_select = queryStringTemplates(
            tabla='Tabla5', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['tarjeta_banco'])

        # Consulta para extraer los datos de la tabla5
        select = self.session.prepare(query_select)
        filas = self.session.execute(select, [tarjeta_banco])
        df_rows = []

        for fila in filas:
            df_rows.append({
                'tarjeta_nombre_banco': fila.tarjeta_banco,
                'tarjeta_nro': str(fila.tarjeta_nro),
                'reservacion_nro': fila.reservacion_nro,
                'reservacion_confirmado': fila.reservacion_confirmado
            })
        return df_rows

    def selectDatosTabla6(self, pelicula_categoria: str=None, pelicula_actor: str=None):
        """
            Descripción: Función para extraer los datos de la tabla6 dado la categoría de la película
        """

        if pelicula_categoria is None:
            pelicula_categoria = input("Ingresa la categoría de la película: ")

        if pelicula_actor is None:
            pelicula_actor = input("Ingresa el autor de la película: ")

        query_select = queryStringTemplates(
            tabla='Tabla6', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True,
            where_columns=['pelicula_categoria', 'pelicula_actor'])

        # Consulta para extraer los datos de la tabla6
        select = self.session.prepare(query_select)
        filas = self.session.execute(select, [pelicula_categoria, pelicula_actor])
        df_rows = []

        for fila in filas:
            df_rows.append({
                'pelicula_categoria': fila.pelicula_categoria,
                'pelicula_nombre': fila.pelicula_nombre,
                'pelicula_actor': fila.pelicula_actor,
                'pelicula_actores': list(fila.pelicula_actores)
            })
        return df_rows

    def selectDatosTabla7(self, usuario_tlf: str=None):
        """
            Descripción: Función para extraer los datos de la tabla7 dado el número de teléfono del usuario
        """

        if usuario_tlf is None:
            usuario_tlf = input("Ingresa el número de teléfono del usuario: ")

        query_select = queryStringTemplates(
            tabla='Tabla7', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['usuario_tlf'])

        # Consulta para extraer los datos de la tabla7
        select = self.session.prepare(query_select)
        filas = self.session.execute(select, [usuario_tlf])
        df_rows = []

        for fila in filas:
            df_rows.append({
                'usuario_tlf': fila.usuario_tlf,
                'usuario_dni': fila.usuario_dni,
                'usuario_nombre': fila.usuario_nombre,
                'usuario_tlfs': list(fila.usuario_tlfs)
            })
        return df_rows

    def selectDatosTabla8(self, ciudad_nombre: str=None):
        """
            Descripción: Función para extraer los datos de la tabla8 dado el nombre de la ciudad
        """

        if ciudad_nombre is None:
            ciudad_nombre = input("Ingresa el nombre de la ciudad: ")

        query_select = queryStringTemplates(
            tabla='Tabla8', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['ciudad_nombre'])

        # Consulta para extraer los datos de la tabla8
        select = self.session.prepare(query_select)
        filas = self.session.execute(select, [ciudad_nombre])
        df_rows = []

        for fila in filas:
            df_rows.append({
                'ciudad_nombre': fila.ciudad_nombre,
                'pelicula_nombre': fila.pelicula_nombre,
                'funcion_fecha_hora': fila.funcion_fecha_hora
            })
        return df_rows
