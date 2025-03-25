import logging

from dataclasses import dataclass
from datetime import datetime

from .selects import Selects
from .utils import TipoOperacion, queryStringTemplates, Logging, pedir_dato

logging.basicConfig(
    format=Logging.MSG_FORMAT.value,
    datefmt=Logging.DATETIME_FORMAT.value, level=logging.INFO,
)

logger = logging.getLogger(Logging.DELETES_LOGGER.value)

@dataclass
class Deletes:
    session: object

    # def eliminar_datos_todas_tables(self):
    #     """
    #         Descripción: Función para eliminar todos los datos de las tablas
    #     """
    #     tablas = [
    #         "SoporteUsuario",
    #         "SoportePelicula",
    #         "SoporteCiudad",
    #         "SoporteSala",
    #         "SoporteCine",
    #         "SoporteTarjeta",
    #         "SoporteTipoBoleto",
    #         "SoporteReservacion",
    #         "CiudadCine",
    #         "CineSala",
    #         "PeliculaFuncion",
    #         "UsuarioReservacion",
    #         "ReservacionTipoBoleto",
    #         "Tabla1",
    #         "Tabla2",
    #         "Tabla3",
    #         "Tabla4",
    #         "Tabla5",
    #         "Tabla6",
    #         "Tabla7",
    #         "Tabla8"
    #     ]

    #     for tabla in tablas:
    #         self.eliminar_datos(tabla)

    # def eliminar_datos(self, tabla: str):
    #     """
    #         Descripción: Función para eliminar todos los datos de una tabla
    #     """
    #     query = queryStringTemplates(
    #         tabla, [], TipoOperacion.DELETE.value, all_records=True)
    #     self.session.execute(query)
    #     logger.info(f"Datos eliminados de la tabla {tabla}")

    def eliminar_registro_tabla1(self, paciente_direccion: str, paciente_nombre: int):
        """
            Descripción: Función para eliminar un registro de la tabla 1
        """
        query = queryStringTemplates(
            'Tabla1', [], TipoOperacion.DELETE.value,
            where_columns=['paciente_nombre'])

        logger.info(f"Delete query: {query}")
        _delete_statement = self.session.prepare(query)
        self.session.execute(_delete_statement, [paciente_nombre])
        logger.info(
            f"Registro con dirección {paciente_direccion} y "
            f"Nombre {paciente_nombre} eliminado de la tabla Tabla1")
