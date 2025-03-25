import logging
import uuid

from dataclasses import dataclass
from datetime import datetime

# from .clases_tablas import Usuario, Pelicula, Ciudad, Cine, Reservacion, Sala, PeliculaFuncion,\
#     Tarjeta, TipoBoleto

from .clases_tablas import SoportePaciente, SoporteMedico

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
    # --- Funciones para insertar datos de tabla1, tabla6 y soporte
    def insertar_paciente(self, **kwargs):
        """
            Descripción: Función para pedir los datos de un paciente y almacenarlos en la base de datos
        """
        dni = int(pedir_dato('paciente_dni', 'Paciente_DNI', 'usuario', **kwargs))
        nombre = pedir_dato('paciente_nombre', 'Paciente_Nombre', 'usuario', **kwargs)

        print(" *** Formato de fecha y hora: YYYYMMDD. Ejemplo: 20210930 ***")
        fecha_hora = pedir_dato('paciente_fecha_nac', 'Paciente_Fecha_Nac', 'usuario', **kwargs)
        _fecha_nac = datetime.strptime(fecha_hora, "%Y%m%d")


        direccion = pedir_dato('paciente_direccion', 'Paciente_Direccion', 'usuario', **kwargs)
        tlf = pedir_dato('paciente_tlf', 'Paciente_Tlf', 'usuario', **kwargs)
        alergias = pedir_datos('paciente_alergias', 'Paciente_Alergias', 'usuario', **kwargs)

        _select_instance = Selects(session=self.session)
        _usuario = _select_instance.selectDatosPaciente(dni)

        if _usuario is None:
            self.insertar_tabla1(
                paciente_dni=dni, paciente_nombre=nombre, paciente_fecha_nac=_fecha_nac,
                paciente_direccion=direccion, paciente_tlf=tlf, paciente_alergias=alergias)
            self.insertar_soporte_paciente(
                paciente_dni=dni, paciente_nombre=nombre, paciente_fecha_nac=_fecha_nac,
                paciente_direccion=direccion, paciente_tlf=tlf, paciente_alergias=alergias)
            
            self.insertar_tabla6(
                paciente_dni=dni, paciente_nombre=nombre, paciente_fecha_nac=_fecha_nac,
                paciente_direccion=direccion, paciente_tlf=tlf, paciente_alergias=alergias)

            _usuario = SoportePaciente(
                dni, nombre, _fecha_nac, direccion, tlf, alergias
            )
        else:
            logger.info(f"\nEl paciente - {str(_usuario)} - ya está en la base de datos.")
        return _usuario

    def insertar_tabla1(self, **kwargs):
        """
            Descripción: Función para insertar datos en la tabla 7
        """
        print(kwargs)
        dni = kwargs['paciente_dni']
        nombre = kwargs['paciente_nombre']
        fecha_nac = kwargs['paciente_fecha_nac']
        direccion = kwargs['paciente_direccion']
        tlf = kwargs['paciente_tlf']
        alergias = kwargs['paciente_alergias']

        # logger.info(f"\nDatos del paciente: {dni}, {nombre}, {fecha_nac}, {direccion}, {tlf}, {alergias}")

        _query_insert_tabla7 = queryStringTemplates(
            tabla='Tabla1', tipo_operacion=TipoOperacion.INSERT.value,
            columnas=['paciente_dni', 'paciente_nombre', 'paciente_fecha_nac', 'paciente_direccion', 'paciente_tlf', 'paciente_alergias'])

        # Inserción de datos
        logger.info(f"\n\t{_query_insert_tabla7}")
        _insert_statement_tabla7 = self.session.prepare(_query_insert_tabla7)
        self.session.execute(_insert_statement_tabla7, [dni, nombre, fecha_nac, direccion, tlf, alergias])
        logger.info("--- Datos insertados en Tabla7\n")

        # # Inserción de datos
        # logger.info(f"\n\t{_query_insert_tabla7}")
        # _insert_statement_tabla7 = self.session.prepare(_query_insert_tabla7)
        # for telefono in telefonos:
        #     self.session.execute(_insert_statement_tabla7, [telefono, dni, nombre, telefonos])
        # logger.info("--- Datos insertados en Tabla7\n")

    def insertar_tabla6(self, **kwargs):
        """
            Descripción: Función para insertar datos en la tabla 6
        """
        dni = kwargs['paciente_dni']
        nombre = kwargs['paciente_nombre']
        fecha_nac = kwargs['paciente_fecha_nac']
        direccion = kwargs['paciente_direccion']
        tlf = kwargs['paciente_tlf']
        alergias = kwargs['paciente_alergias']

        # logger.info(f"\nDatos del paciente: {dni}, {nombre}, {fecha_nac}, {direccion}, {tlf}, {alergias}")

        _query_insert_tabla6 = queryStringTemplates(
            tabla='Tabla6', tipo_operacion=TipoOperacion.INSERT.value,
            columnas=['paciente_alergia', 'paciente_dni', 'paciente_nombre', 'paciente_fecha_nac', 'paciente_direccion', 'paciente_tlf'])
        
        # Inserción de datos
        logger.info(f"\n\t{_query_insert_tabla6}")
        _insert_statement_tabla6 = self.session.prepare(_query_insert_tabla6)
        for alergia in alergias:
            if alergia.strip() == "":
                continue
            self.session.execute(
                _insert_statement_tabla6, [alergia, dni, nombre, fecha_nac, direccion, tlf])
        logger.info("--- Datos insertados en Tabla6\n")

    def insertar_soporte_paciente(self, **kwargs):
        """
            Descripción: Función para insertar datos en la tabla SoporteUsuario
        """
        dni = kwargs['paciente_dni']
        nombre = kwargs['paciente_nombre']
        fecha_nac = kwargs['paciente_fecha_nac']
        direccion = kwargs['paciente_direccion']
        tlf = kwargs['paciente_tlf']
        alergias = kwargs['paciente_alergias']

        # logger.info(f"\nDatos del paciente: {dni}, {nombre}, {fecha_nac}, {direccion}, {tlf}, {alergias}")

        _query_insert_soporte_usuario = queryStringTemplates(
            tabla='soportepaciente', tipo_operacion=TipoOperacion.INSERT.value,
            columnas=[
                'paciente_dni', 'paciente_nombre', 'paciente_fecha_nac',
                'paciente_direccion', 'paciente_tlf', 'paciente_alergias'])

        # Inserción de datos
        logger.info(f"\n\t{_query_insert_soporte_usuario}")
        _insert_statement_soporte_usuario = self.session.prepare(_query_insert_soporte_usuario)
        self.session.execute(_insert_statement_soporte_usuario, [dni, nombre, fecha_nac, direccion, tlf, alergias])
        logger.info("--- Datos insertados en SoportePaciente\n")


    # --- Creación de métodos de inserción de datos - 2

    def insertar_medico(self, **kwargs):
        """
            Descripción: Función para pedir los datos de un medico
        """
        dni = int(pedir_dato('medico_dni', 'Medico_DNI', 'medico', **kwargs))
        nombre = pedir_dato('medico_nombre', 'Medico_Nombre', 'medico', **kwargs)

        print(" *** Formato de fecha y hora: YYYYMMDD. Ejemplo: 20210930 ***")
        fecha_nac = pedir_dato('medico_fecha_nac', 'Medico_Fecha_Nac', 'medico', **kwargs)
        _fecha_nac = datetime.strptime(fecha_nac, "%Y%m%d")
        
        tlf = pedir_dato('medico_tlf', 'Medico_Tlf', 'medico', **kwargs)
        especialidad = pedir_datos('medico_especialidades', 'Medico_Especialidades', 'medico', **kwargs)
        # logger.info(f"\nDatos del medico: {dni}, {nombre}, {fecha_nac}, {tlf}, {especialidad}")

        _select_instance = Selects(session=self.session)
        medico = _select_instance.selectDatosMedico(dni)

        # Si el medico no está en la base de datos, lo insertamos
        if medico is None:
            self.insertar_soporte_medico(
                medico_dni=dni, medico_nombre=nombre, medico_fecha_nac=_fecha_nac, medico_tlf=tlf, medico_especialidades=especialidad)

            medico = SoporteMedico(
                dni, nombre, _fecha_nac, tlf, especialidad
            )
        else:
            logger.info(f"\nEl medico - {str(medico)} - ya está en la base de datos.")
        return medico

    def insertar_soporte_medico(self, **kwargs):
        """
            Descripción: Función para insertar datos en la tabla SoporteMedico
        """
        dni = kwargs['medico_dni']
        nombre = kwargs['medico_nombre']
        fecha_nac = kwargs['medico_fecha_nac']
        tlf = kwargs['medico_tlf']
        especialidades = kwargs['medico_especialidades']
        
        # logger.info(f"\nDatos de la película: {nombre}, {categoria}, {actores}")

        _query_insert_soporte_medico = queryStringTemplates(
            tabla='soportemedico', tipo_operacion=TipoOperacion.INSERT.value,
            columnas=['medico_dni', 'medico_nombre', 'medico_fecha_nac', 'medico_tlf', 'medico_especialidades'])

        # Inserción de datos
        logger.info(f"\n\t{_query_insert_soporte_medico}")
        _insert_statement_soporte_medico = self.session.prepare(_query_insert_soporte_medico)
        self.session.execute(_insert_statement_soporte_medico, [dni, nombre, fecha_nac, tlf, especialidades])
        logger.info("--- Datos insertados en SoporteMedico\n")
