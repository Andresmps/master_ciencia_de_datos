import logging

from dataclasses import dataclass
from datetime import datetime

# from .clases_tablas import Usuario, Pelicula, Ciudad, Cine, Reservacion, TipoBoleto,\
#     CiudadCine, CineSala, Tarjeta, PeliculaFuncion, Sala
from .clases_tablas import SoportePaciente, SoporteMedico
from .utils import TipoOperacion, queryStringTemplates, Logging

logging.basicConfig(
    format=Logging.MSG_FORMAT.value,
    datefmt=Logging.DATETIME_FORMAT.value, level=logging.INFO,
)

logger = logging.getLogger(Logging.SELECTS_LOGGER.value)

@dataclass
class Selects:
    session: object

    def selectDatosPaciente(self, usuario_dni: str=None):
        """
            Descripción: Función para extraer los datos del usuario dado su dni
        """

        if usuario_dni is None:
            usuario_dni = int(input("Ingresa el DNI del paciente: "))

        _usuario = None
        query_select_usuario = queryStringTemplates(
            tabla='soportepaciente', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['Paciente_DNI'])

        # Consulta para extraer los datos del usuario
        select = self.session.prepare(query_select_usuario)
        filas = self.session.execute(select, [usuario_dni])

        if not filas:
            logger.info(f"No se encontró el usuario con el DNI={usuario_dni}\n")
            return _usuario

        # Como usuario_dni es clave primaria, solo se espera un resultado
        for fila in filas:
            _usuario = SoportePaciente(
                fila.paciente_dni, fila.paciente_nombre, fila.paciente_fecha_nac,
                fila.paciente_direccion, fila.paciente_tlf, fila.paciente_alergias
            )
            logger.info(f"\n\tPaciente encontrado - {_usuario}\n")

        return _usuario

    def selectDatosMedico(self, medico_dni: str=None):
        """
            Descripción: Función para extraer los datos del medico dado su dni
        """

        if medico_dni is None:
            medico_dni = int(input("Ingresa el dni del medico: "))

        _medico = None
        query_select_medico = queryStringTemplates(
            tabla='soportemedico', tipo_operacion=TipoOperacion.SELECT.value,
            columnas=[], all_columns=True, where_columns=['medico_dni'])

        # Consulta para extraer los datos del medico
        select = self.session.prepare(query_select_medico)
        filas = self.session.execute(select, [medico_dni])

        if not filas:
            logger.info(f"No se encontró el medico con el dni={medico_dni}\n")
            return _medico

        # Como pelicula_nombre es clave primaria, solo se espera un resultado
        for fila in filas:
            _medico = SoporteMedico(
                fila.medico_dni, fila.medico_nombre, fila.medico_fecha_nac,
                fila.medico_tlf, fila.medico_especialidades
            )
            logger.info(f"\n\tMedico encontrado - {_medico}\n")

        return _medico
