import logging
import uuid

from dataclasses import dataclass
from datetime import datetime

from .clases_tablas import Usuario, Pelicula, Ciudad, Cine, Reservacion, Sala, PeliculaFuncion,\
    Tarjeta, TipoBoleto
from .selects import Selects
from .utils import TipoOperacion, queryStringTemplates, Logging, pedir_dato, pedir_datos

logging.basicConfig(
    format=Logging.MSG_FORMAT.value,
    datefmt=Logging.DATETIME_FORMAT.value, level=logging.INFO,
)

logger = logging.getLogger(Logging.INSERTS_LOGGER.value)

@dataclass
class Inserts:
    session: object

    # --- Creación de métodos de inserción de datos - 1
    # --- Funciones para insertar datos de usuarios y tabla 7
    def insertar_usuario(self, **kwargs):
        """
            Descripción: Función para pedir los datos de un usuario y almacenarlos en la base de datos
        """
        dni = pedir_dato('dni', 'DNI', 'usuario', **kwargs)
        nombre = pedir_dato('nombre', 'nombre', 'usuario', **kwargs)
        telefonos = pedir_datos('telefonos', 'teléfono', 'usuario', **kwargs)

        _select_instance = Selects(session=self.session)
        _usuario = _select_instance.selectDatosUsuario(dni)

        if _usuario is None:
            self.insertar_tabla7(usuario_dni=dni, usuario_nombre=nombre, usuario_tlfs=telefonos)
            self.insertar_soporte_usuario(
                usuario_dni=dni, usuario_nombre=nombre, usuario_tlfs=telefonos)

            _usuario = Usuario(dni=dni, nombre=nombre, tlfs=telefonos)
        else:
            logger.info(f"\nEl usuario - {str(_usuario)} - ya está en la base de datos.")
        return _usuario

    def insertar_tabla7(self, **kwargs):
        """
            Descripción: Función para insertar datos en la tabla 7
        """
        dni = kwargs['usuario_dni']
        nombre = kwargs['usuario_nombre']
        telefonos = kwargs['usuario_tlfs']

        # logger.info(f"\nDatos del usuario: {dni}, {nombre}, {telefonos}")

        _query_insert_tabla7 = queryStringTemplates(
            tabla='Tabla7', tipo_operacion=TipoOperacion.INSERT.value,
            columnas=['usuario_tlf', 'usuario_dni', 'usuario_nombre', 'usuario_tlfs'])

        # Inserción de datos
        logger.info(f"\n\t{_query_insert_tabla7}")
        _insert_statement_tabla7 = self.session.prepare(_query_insert_tabla7)
        for telefono in telefonos:
            self.session.execute(_insert_statement_tabla7, [telefono, dni, nombre, telefonos])
        logger.info("--- Datos insertados en Tabla7\n")

    def insertar_soporte_usuario(self, **kwargs):
        """
            Descripción: Función para insertar datos en la tabla SoporteUsuario
        """
        dni = kwargs['usuario_dni']
        nombre = kwargs['usuario_nombre']
        telefonos = kwargs['usuario_tlfs']

        # logger.info(f"\nDatos del usuario: {dni}, {nombre}, {telefonos}")

        _query_insert_soporte_usuario = queryStringTemplates(
            tabla='SoporteUsuario', tipo_operacion=TipoOperacion.INSERT.value,
            columnas=['usuario_dni', 'usuario_nombre', 'usuario_tlfs'])

        # Inserción de datos
        logger.info(f"\n\t{_query_insert_soporte_usuario}")
        _insert_statement_soporte_usuario = self.session.prepare(_query_insert_soporte_usuario)
        self.session.execute(_insert_statement_soporte_usuario, [dni, nombre, telefonos])
        logger.info("--- Datos insertados en SoporteUsuario\n")


    # --- Creación de métodos de inserción de datos - 2
    # --- Funciones para insertar datos de película, tabla 1, tabla 6 y peliculaSoporte

    def insertar_pelicula(self, **kwargs):
        """
            Descripción: Función para pedir los datos de una película y almacenarlos en la base de datos
        """
        nombre = pedir_dato('nombre', 'nombre', 'pelicula', **kwargs)
        categoria = pedir_dato('categoria', 'categoría', 'pelicula', **kwargs)
        actores = pedir_datos('actores', 'actor', 'pelicula', **kwargs)

        # logger.info(f"\nDatos de la película: {nombre}, {categoria}, {actores}")

        _select_instance = Selects(session=self.session)
        pelicula = _select_instance.selectDatosPelicula(nombre)

        # Si la película no está en la base de datos, la insertamos
        if pelicula is None:
            self.insertar_tabla1(categoria=categoria, nombre=nombre, actores=actores)
            self.insertar_tabla6(categoria=categoria, nombre=nombre, actores=actores)
            self.insertar_pelicula_soporte(categoria=categoria, nombre=nombre, actores=actores)

            pelicula = Pelicula(nombre, categoria, actores)
        else:
            logger.info(f"\nLa película - {pelicula} - ya está en la base de datos.")
        return pelicula

    def insertar_tabla1(self, **kwargs):
        """
            Descripción: Función para insertar datos en la tabla 1
        """
        categoria = kwargs['categoria']
        nombre = kwargs['nombre']
        actores = kwargs['actores']

        # logger.info(f"\nDatos de la película: {nombre}, {categoria}, {actores}")

        _query_insert_tabla1 = queryStringTemplates(
            tabla='Tabla1', tipo_operacion=TipoOperacion.INSERT.value,
            columnas=['pelicula_categoria', 'pelicula_nombre', 'pelicula_actores'])

        # Inserción de datos
        logger.info(f"\n\t{_query_insert_tabla1}")
        _insert_statement_tabla1 = self.session.prepare(_query_insert_tabla1)
        self.session.execute(_insert_statement_tabla1, [categoria, nombre, actores])
        logger.info("--- Datos insertados en Tabla1")

    def insertar_tabla6(self, **kwargs):
        """
            Descripción: Función para insertar datos en la tabla 6
        """
        categoria = kwargs['categoria']
        nombre = kwargs['nombre']
        actores = kwargs['actores']

        # logger.info(f"\nDatos de la película: {nombre}, {categoria}, {actores}")

        _query_insert_tabla6 = queryStringTemplates(
            tabla='Tabla6', tipo_operacion=TipoOperacion.INSERT.value,
            columnas=['pelicula_categoria', 'pelicula_actor', 'pelicula_nombre', 'pelicula_actores'])

        # Inserción de datos
        logger.info(f"\n\t{_query_insert_tabla6}")
        _insert_statement_tabla6 = self.session.prepare(_query_insert_tabla6)
        for actor in actores:
            self.session.execute(_insert_statement_tabla6, [categoria, actor, nombre, actores])
        logger.info("--- Datos insertados en Tabla6")

    def insertar_pelicula_soporte(self, **kwargs):
        """
            Descripción: Función para insertar datos en la tabla SoportePelicula
        """
        nombre = kwargs['nombre']
        categoria = kwargs['categoria']
        actores = kwargs['actores']

        # logger.info(f"\nDatos de la película: {nombre}, {categoria}, {actores}")

        _query_insert_pelicula = queryStringTemplates(
            tabla='SoportePelicula', tipo_operacion=TipoOperacion.INSERT.value,
            columnas=['pelicula_nombre', 'pelicula_categoria', 'pelicula_actores'])

        # Inserción de datos
        logger.info(f"\n\t{_query_insert_pelicula}")
        _insert_statement_pelicula = self.session.prepare(_query_insert_pelicula)
        self.session.execute(_insert_statement_pelicula, [nombre, categoria, actores])
        logger.info("--- Datos insertados en SoportePelicula")

    # --- Creación de métodos de inserción de datos - 3
    # --- Funciones para insertar datos de Cine, Ciudad y CiudadCine, CineSoporte
    def insertar_ciudad_adquirir_datos(self, **kwargs):
        """
            Descripción: Función para pedir los datos de un cine y almacenarlos en la base de datos
        """
        nombre = pedir_dato('nombre', 'nombre', 'ciudad', **kwargs)
        provincia = pedir_dato('provincia', 'provincia', 'ciudad', **kwargs)
        comunidad_autonoma = pedir_dato('comunidad_autonoma', 'comunidad autónoma', 'ciudad', **kwargs)

        _select_instance = Selects(session=self.session)
        ciudad = _select_instance.selectDatosCiudad(nombre)

        # Si la ciudad no está en la base de datos, la insertamos
        if ciudad is None:
            self.insertar_ciudad(
                nombre=nombre, provincia=provincia, comunidad_autonoma=comunidad_autonoma)

            ciudad = Ciudad(nombre, provincia, comunidad_autonoma)
        else:
            logger.info(f"\nLa ciudad - {ciudad} - ya está en la base de datos.")
        return ciudad

    def insertar_ciudad(self, **kwargs):
        """
            Descripción: Función para pedir los datos de un cine y almacenarlos en la base de datos
        """
        nombre = kwargs['nombre']
        provincia = kwargs['provincia']
        comunidad_autonoma = kwargs['comunidad_autonoma']

        # logger.info(f"\nDatos de la ciudad: {nombre}, {provincia}, {comunidad_autonoma}")

        _query_insert_ciudad = queryStringTemplates(
            tabla='SoporteCiudad', tipo_operacion=TipoOperacion.INSERT.value,
            columnas=['ciudad_nombre', 'ciudad_provincia', 'ciudad_comunidad_autonoma'])

        # Inserción de datos Ciudad
        logger.info(f"\n\t{_query_insert_ciudad}")
        _insert_statement_ciudad = self.session.prepare(_query_insert_ciudad)
        self.session.execute(_insert_statement_ciudad, [nombre, provincia, comunidad_autonoma])
        logger.info("--- Datos insertados en Ciudad")

    def insertar_cine(self, **kwargs):
        """
            Descripción: Función para pedir los datos de un cine y almacenarlos en la base de datos
        """
        id = str(uuid.uuid4()) if kwargs.get('id', None) is None else kwargs['id']
        nombre = pedir_dato('nombre', 'nombre', 'cine', **kwargs)
        ubicacion = pedir_dato('ubicacion', 'ubicación', 'cine', **kwargs)
        ciudad_nombre = pedir_dato('ciudad_nombre', 'ciudad', 'ciudad', **kwargs)

        _select_instance = Selects(session=self.session)
        ciudad = _select_instance.selectDatosCiudad(ciudad_nombre)
        # logger.info(f"Datos de la ciudad: {ciudad}")

        # Si la ciudad no está en la base de datos, no insertamos el cine
        if ciudad is None:
            logger.info(
                "La ciudad no está en la base de datos. Por favor, inserte la ciudad primero.\n")

            crear_ciudad = input("¿Desea insertar la ciudad? (si/no): ")
            if crear_ciudad.lower() == "si":
                ciudad = self.insertar_ciudad()
            else:
                return

        cine = _select_instance.selectDatosCine(id)
        # logger.info(f"Datos de la cine: {cine}")

        # Si el cine no está en la base de datos, lo insertamos
        if cine is None:
            # Preparación de consultas para insertar datos
            _query_insert_soport_cine = queryStringTemplates(
                tabla='SoporteCine', tipo_operacion=TipoOperacion.INSERT.value,
                columnas=['cine_id', 'cine_nombre', 'cine_ubicacion'])

            _query_insert_ciudad_cine = queryStringTemplates(
                tabla='CiudadCine', tipo_operacion=TipoOperacion.INSERT.value,
                columnas=['cine_id', 'ciudad_nombre'])

            logger.info(f"\n\t{_query_insert_soport_cine}")
            _insert_statement_cine = self.session.prepare(_query_insert_soport_cine)
            self.session.execute(_insert_statement_cine, [id, nombre, ubicacion])
            logger.info("--- Datos insertados en SoporteCine")

            # Inserción de datos CiudadCine
            logger.info(f"\n\t{_query_insert_ciudad_cine}")
            _insert_statement_ciudad_cine = self.session.prepare(_query_insert_ciudad_cine)
            self.session.execute(_insert_statement_ciudad_cine, [id, ciudad_nombre])
            logger.info("--- Datos insertados en CiudadCine")

            cine = Cine(id, nombre, ubicacion)
        else:
            logger.info(f"\nEl cine - {cine} - ya está en la base de datos.")
        return cine

    # --- Creación de métodos de inserción de datos - 4
    # --- Funciones para insertar datos en la relación reserva compra, y entidades
    #       reservacion, y tipo_boleto

    def insertar_sala(self, **kwargs):
        """
            Descripción: Función para pedir los datos de un cine y almacenarlos en la base de datos
        """
        _select_instance = Selects(session=self.session)

        nro = pedir_dato('IdNroSala', 'número de sala', 'sala', **kwargs)
        nro = int(nro)
        capacidad = pedir_dato('capacidad', 'capacidad', 'sala', **kwargs)
        cine_id = pedir_dato('cine_id', 'id del cine', 'cine', **kwargs)

        _cine = _select_instance.selectDatosCine(cine_id)

        if _cine is None:
            logger.info(
                "El cine no está en la base de datos. Por favor, inserte el cine primero.\n")

            crear_cine = input("¿Desea insertar el cine? (si/no): ")
            if crear_cine.lower() == "si":
                _cine = self.insertar_cine()
            else:
                return

        sala = _select_instance.selectDatosSala(nro)

        # Si la sala no está en la base de datos, la insertamos
        if sala is None:
            # Preparación de consultas para insertar datos
            _query_insert_sala = queryStringTemplates(
                tabla='SoporteSala', tipo_operacion=TipoOperacion.INSERT.value,
                columnas=['sala_nro', 'capacidad'])

            _query_insert_sala_ciudad = queryStringTemplates(
                tabla='CineSala', tipo_operacion=TipoOperacion.INSERT.value,
                columnas=['sala_nro', 'cine_id'])

            _query_insert_tabla_3 = queryStringTemplates(
                tabla='Tabla3', tipo_operacion=TipoOperacion.INSERT.value,
                columnas=['cine_nombre', 'sala_nro'])

            # Inserción de datos Sala
            logger.info(f"\n\t{_query_insert_sala}")
            _insert_statement_sala = self.session.prepare(_query_insert_sala)
            self.session.execute(_insert_statement_sala, [nro, capacidad])
            logger.info("--- Datos insertados en SoporteSala")

            # Inserción de datos SalaCiudad
            logger.info(f"\n\t{_query_insert_sala_ciudad}")
            _insert_statement_sala_ciudad = self.session.prepare(_query_insert_sala_ciudad)
            self.session.execute(
                _insert_statement_sala_ciudad, [nro, _cine.IdCine])
            logger.info("--- Datos insertados en SoporteSalaCiudad")

            # Inserción de datos Tabla3
            logger.info(f"\n\t{_query_insert_tabla_3}")
            _insert_statement_tabla3 = self.session.prepare(_query_insert_tabla_3)
            self.session.execute(_insert_statement_tabla3, [_cine.nombre, nro])
            logger.info("--- Datos insertados en Tabla3")

            sala = Sala(nro, capacidad)
        else:
            logger.info(f"\nLa sala - {sala} - ya está en la base de datos.")
        return sala

    def insertar_funcion(self, **kwargs):
        """
            Descripción: Función para pedir los datos de un cine y almacenarlos en la base de datos
        """
        _select_instance = Selects(session=self.session)

        print(" *** Formato de fecha y hora: YYYYMMDD_HHMM. Ejemplo: 20210930_1500 ***")
        fecha_hora = pedir_dato('IdFechaHoraFuncion', 'fecha y hora', 'función', **kwargs)
        _fecha_hora = datetime.strptime(fecha_hora, "%Y%m%d_%H%M")

        sala_nro = pedir_dato('sala_nro', 'número de sala', 'sala', **kwargs)
        sala_nro = int(sala_nro)

        sala = _select_instance.selectDatosSala(sala_nro)

        if sala is None:
            logger.info(
                "La sala no está en la base de datos. Por favor, inserte la sala primero.\n")

            crear_sala = input("¿Desea insertar la sala? (si/no): ")
            if crear_sala.lower() == "si":
                sala = self.insertar_sala()
            else:
                return

        _cine = _select_instance.selectDatosCineSala(sala_nro)
        _ciudad = _select_instance.selectDatosCiudadCine(_cine.IdCine)

        pelicula_nombre = pedir_dato('IdNombrePelicula', 'pelicula_nombre', 'película', **kwargs)
        _pelicula = _select_instance.selectDatosPelicula(pelicula_nombre)

        if _pelicula is None:
            logger.info(
                "La película no está en la base de datos. Por favor, inserte la película primero.\n")

            crear_pelicula = input("¿Desea insertar la película? (si/no): ")
            if crear_pelicula.lower() == "si":
                _pelicula = self.insertar_pelicula()
            else:
                return

        funcion = _select_instance.selectDatosPeliculaFuncion(_fecha_hora)
        # logger.info(f"Fecha y hora de la función: {_fecha_hora}")

        # Si la función no está en la base de datos, la insertamos
        if funcion is None:
            # Preparación de consultas para insertar datos
            _query_insert_funcion = queryStringTemplates(
                tabla='PeliculaFuncion', tipo_operacion=TipoOperacion.INSERT.value,
                columnas=['funcion_fecha_hora', 'porcentaje_ocupacion', 'pelicula_nombre'])

            _query_insert_tabla8 = queryStringTemplates(
                tabla='Tabla8', tipo_operacion=TipoOperacion.INSERT.value,
                columnas=['ciudad_nombre', 'pelicula_nombre', 'funcion_fecha_hora'])

            # Inserción de datos Función
            logger.info(f"\n\t{_query_insert_funcion}")
            _insert_statement_funcion = self.session.prepare(_query_insert_funcion)
            self.session.execute(_insert_statement_funcion, [_fecha_hora, "0", pelicula_nombre])
            logger.info("--- Datos insertados en PeliculaFuncion")

            # Inserción de datos Tabla8
            logger.info(f"\n\t{_query_insert_tabla8}")
            _insert_statement_tabla8 = self.session.prepare(_query_insert_tabla8)
            self.session.execute(
                _insert_statement_tabla8, [_ciudad.IdNombreCiudad, pelicula_nombre, _fecha_hora])

            funcion = PeliculaFuncion(_fecha_hora, pelicula_nombre, "0")
        else:
            logger.info(f"\nLa función - {funcion} - ya está en la base de datos.")

        return funcion

    def insertar_tarjeta(self, **kwargs):
        """
            Descripción: Función para pedir los datos de un cine y almacenarlos en la base de datos
        """
        _select_instance = Selects(session=self.session)

        nro = pedir_dato('IdNroTarjeta', 'número de tarjeta', 'tarjeta', **kwargs)
        nro = int(nro)

        print(" *** Formato de fecha: YYYY-MM. Por ejemplo: 2021-09 ***")
        fecha = pedir_dato('fecha', 'fecha', 'tarjeta', **kwargs)
        banco = pedir_dato('banco', 'banco', 'tarjeta', **kwargs)

        tarjeta = _select_instance.selectDatosTarjeta(nro)

        # Si la tarjeta no está en la base de datos, la insertamos
        if tarjeta is None:
            # Preparación de consultas para insertar datos
            _query_insert_tarjeta = queryStringTemplates(
                tabla='SoporteTarjeta', tipo_operacion=TipoOperacion.INSERT.value,
                columnas=['tarjeta_nro', 'tarjeta_fecha', 'tarjeta_banco'])

            # Inserción de datos Tarjeta
            logger.info(f"\n\t{_query_insert_tarjeta}")
            _insert_statement_tarjeta = self.session.prepare(_query_insert_tarjeta)
            self.session.execute(_insert_statement_tarjeta, [nro, fecha, banco])
            logger.info("--- Datos insertados en SoporteTarjeta")
            tarjeta = Tarjeta(nro, fecha, banco)
        else:
            logger.info(f"\nLa tarjeta - {tarjeta} - ya está en la base de datos.")
        return tarjeta

    def insertar_tipo_boleto(self, **kwargs):
        """
            Descripción: Función para pedir los datos de un cine y almacenarlos en la base de datos
        """
        _select_instance = Selects(session=self.session)

        nombre = pedir_dato('IdNombreTipoBoleto', 'nombre', 'tipo de boleto', **kwargs)
        descuento = pedir_dato('descuento', 'descuento', 'tipo de boleto', **kwargs)
        descuento = int(descuento)

        tipo_boleto = _select_instance.selectDatosTipoBoleto(nombre)

        # Si el tipo de boleto no está en la base de datos, lo insertamos
        if tipo_boleto is None:
            # Preparación de consultas para insertar datos
            _query_insert_tipo_boleto = queryStringTemplates(
                tabla='SoporteTipoBoleto', tipo_operacion=TipoOperacion.INSERT.value,
                columnas=['tipo_boleto', 'descuento'])

            # Inserción de datos TipoBoleto
            logger.info(f"\n\t{_query_insert_tipo_boleto}")
            _insert_statement_tipo_boleto = self.session.prepare(_query_insert_tipo_boleto)
            self.session.execute(_insert_statement_tipo_boleto, [nombre, descuento])
            logger.info("--- Datos insertados en SoporteTipoBoleto")
            tipo_boleto = TipoBoleto(nombre, descuento)
        else:
            logger.info(f"\nEl tipo de boleto - {tipo_boleto} - ya está en la base de datos.")
        return tipo_boleto

    def insertar_reservacion(self, **kwargs):
        """
            Descripción: Función para pedir los datos de un cine y almacenarlos en la base de datos
        """
        _select_instance = Selects(session=self.session)
        print(kwargs)
        nro = pedir_dato('IdNroReservacion', 'número de reservación', 'reservación', **kwargs)

        if kwargs.get('confirmado', None) is None:
            confirmado = input("Indica si se ha confirmado la reserva (si := True, no := False): ")
            confirmado = True if confirmado.lower() == "si" else False
        else:
            confirmado = bool(kwargs['confirmado'])

        # Adquisición de los datos del usuario, y validación de que esté en la base de datos
        usuario_dni = pedir_dato('usuario_dni', 'dni del usuario', 'usuario', **kwargs)
        usuario = _select_instance.selectDatosUsuario(usuario_dni)

        if usuario is None:
            logger.info(
                "El usuario no está en la base de datos. Por favor, inserte el usuario primero.\n")

            crear_usuario = input("¿Desea insertar el usuario? (si/no): ")
            if crear_usuario.lower() == "si":
                usuario = self.insertar_usuario()
            else:
                return

        logger.info(" *** Formato de fecha y hora: YYYYMMDD_HHMM. Ejemplo: 20210930_1500 ***")

        if kwargs.get('IdFechaHoraFuncion', None) is not None:
            funcion_fecha_hora = kwargs['IdFechaHoraFuncion']
            _fecha_hora = datetime.strptime(funcion_fecha_hora, "%Y%m%d_%H%M")
        else:
            while True:
                funcion_fecha_hora = input("Ingresa la fecha y hora de la función: ")
                try:
                    _fecha_hora = datetime.strptime(funcion_fecha_hora, "%Y%m%d_%H%M")
                    break
                except Exception as e:
                    print("Error en el formato de la fecha y hora. Inténtelo de nuevo.")

        _funcion = _select_instance.selectDatosPeliculaFuncion(_fecha_hora)

        if _funcion is None:
            logger.info(
                "La función no está en la base de datos. Por favor, inserte la función primero.\n")

            crear_funcion = input("¿Desea insertar la función? (si/no): ")
            if crear_funcion.lower() == "si":
                _funcion = self.insertar_funcion()
            else:
                return

        tarjetas = []
        logger.info(
            "\nIngresa los números de tarjeta de crédito de la reserva. (\".\" para detener la ejecución)\n")

        if kwargs.get('tarjetas', None) is not None:
            tarjetas = kwargs['tarjetas']
            tarjetas = [
                _select_instance.selectDatosTarjeta(int(tarjeta)) for tarjeta in tarjetas]
        else:
            while True:
                tarjeta = input("Número de tarjeta: ")

                if tarjeta == ".":
                    break

                tarjeta = int(tarjeta)
                _tarjeta = _select_instance.selectDatosTarjeta(tarjeta)

                if _tarjeta is None:
                    logger.info(
                        "El número de tarjeta no está en la base de datos. " +
                        "Por favor, inserte un número de tarjeta válido.")

                    crear_tarjeta = input("¿Desea insertar la tarjeta? (si/no): ")
                    if crear_tarjeta.lower() == "si":
                        _tarjeta = self.insertar_tarjeta()
                    else:
                        continue
                tarjetas.append(_tarjeta)

        # Petición de los tipos de boletos, y validación de que estén en la base de datos
        tipo_boletos = {}
        logger.info(
            "Ingresa los tipos de boletos de la reserva. (\".\" para detener la ejecución)\n")

        if kwargs.get('tipos_boletas', None) is not None:
            tipo_boletos = kwargs['tipos_boletas']
        else:
            while True:
                _tipo_boleto = input("Tipo boleto: ")

                if _tipo_boleto == ".":
                    break

                _tipo_boleto_tmp = _select_instance.selectDatosTipoBoleto(_tipo_boleto)

                if _tipo_boleto_tmp is None:
                    logger.info(
                        "El nombre del tipo de boleto no está en la base de datos. " +
                        "Por favor, inserte un nombre de tipo de boleto válido.")
                    crear_tipo_boleto = input("¿Desea insertar el tipo de boleto? (si/no): ")
                    if crear_tipo_boleto.lower() == "si":
                        _tipo_boleto_tmp = self.insertar_tipo_boleto()
                    else:
                        continue
                if _tipo_boleto not in tipo_boletos:
                    tipo_boletos[_tipo_boleto] = 1
                else:
                    tipo_boletos[_tipo_boleto] += 1

        reservacion = _select_instance.selectDatosReservacion(nro)

        # Si la reservación no está en la base de datos, la insertamos
        if reservacion is None:

            _query_insert_tabla2 = queryStringTemplates(
                tabla='Tabla2', tipo_operacion=TipoOperacion.INSERT.value,
                columnas=['usuario_dni', 'reservacion_nro', 'tipo_boleto_nombre'])

            logger.info(f"\n\t{_query_insert_tabla2}")
            _insert_statement_tabla2 = self.session.prepare(_query_insert_tabla2)
            for tipo_boleto in tipo_boletos:
                self.session.execute(_insert_statement_tabla2, [usuario_dni, nro, tipo_boleto])
            logger.info("--- Datos insertados en Tabla2")

            _query_insert_tabla4 = queryStringTemplates(
                tabla='Tabla4', tipo_operacion=TipoOperacion.UPDATE.value,
                columnas=[], update_column="reservacion_nro",
                where_columns=["usuario_dni"], is_counter=True)

            logger.info(f"\n\t{_query_insert_tabla4}")
            _insert_statement_tabla4 = self.session.prepare(_query_insert_tabla4)
            self.session.execute(_insert_statement_tabla4, [usuario_dni])
            logger.info("--- Datos actualizados en Tabla4")

            _query_insert_tabla5 = queryStringTemplates(
                tabla='Tabla5', tipo_operacion=TipoOperacion.INSERT.value,
                columnas=['tarjeta_banco', 'tarjeta_nro', 'reservacion_nro', 'reservacion_confirmado'])

            logger.info(f"\n\t{_query_insert_tabla5}")
            _insert_statement_tabla5 = self.session.prepare(_query_insert_tabla5)
            for tarjeta in tarjetas:
                self.session.execute(
                    _insert_statement_tabla5,
                    [tarjeta.banco, tarjeta.IdNroTarjeta, nro, confirmado])
            logger.info("--- Datos insertados en Tabla5")

            _query_insert_usuario_reservacion = queryStringTemplates(
                tabla='UsuarioReservacion', tipo_operacion=TipoOperacion.INSERT.value,
                columnas=['usuario_dni', 'usuario_nombre', 'reservacion_nro'])

            logger.info(f"\n\t{_query_insert_usuario_reservacion}")
            _insert_statement_usuario_reservacion = self.session.prepare(_query_insert_usuario_reservacion)
            self.session.execute(_insert_statement_usuario_reservacion, [usuario_dni, usuario.nombre, nro])
            logger.info("--- Datos insertados en UsuarioReservacion")

            _query_insert_reservacion_tipo_boleto = queryStringTemplates(
                tabla='ReservacionTipoBoleto', tipo_operacion=TipoOperacion.INSERT.value,
                columnas=['reservacion_nro', 'tipo_boleto_nombre', 'nro_boletos'])

            logger.info(f"\n\t{_query_insert_reservacion_tipo_boleto}")
            _insert_statement_reservacion_tipo_boleto = self.session.prepare(_query_insert_reservacion_tipo_boleto)
            for tipo_boleto, count in tipo_boletos.items():
                self.session.execute(_insert_statement_reservacion_tipo_boleto, [nro, tipo_boleto, count])
            logger.info("--- Datos insertados en ReservacionTipoBoleto")

            _query_insert_soporte_reservacion = queryStringTemplates(
                tabla='SoporteReservacion', tipo_operacion=TipoOperacion.INSERT.value,
                columnas=['reservacion_nro', 'reservacion_confirmado', 'funcion_fecha_hora', 'pelicula_nombre'])

            logger.info(f"\n\t{_query_insert_soporte_reservacion}")
            _insert_statement_soporte_reservacion = self.session.prepare(_query_insert_soporte_reservacion)
            self.session.execute(
                _insert_statement_soporte_reservacion,
                [nro, confirmado, _fecha_hora, _funcion.IdNombrePelicula])
            logger.info("--- Datos insertados en SoporteReservacion")

            reservacion = Reservacion(nro, confirmado, _fecha_hora, _funcion.IdNombrePelicula)
        else:
            print(f"\nLa reservación - {reservacion} - ya está en la base de datos.")
        return reservacion
