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

    def eliminar_datos_todas_tables(self):
        """
            Descripción: Función para eliminar todos los datos de las tablas
        """
        tablas = [
            "SoporteUsuario",
            "SoportePelicula",
            "SoporteCiudad",
            "SoporteSala",
            "SoporteCine",
            "SoporteTarjeta",
            "SoporteTipoBoleto",
            "SoporteReservacion",
            "CiudadCine",
            "CineSala",
            "PeliculaFuncion",
            "UsuarioReservacion",
            "ReservacionTipoBoleto",
            "Tabla1",
            "Tabla2",
            "Tabla3",
            "Tabla4",
            "Tabla5",
            "Tabla6",
            "Tabla7",
            "Tabla8"
        ]

        for tabla in tablas:
            self.eliminar_datos(tabla)

    def eliminar_datos(self, tabla: str):
        """
            Descripción: Función para eliminar todos los datos de una tabla
        """
        query = queryStringTemplates(
            tabla, [], TipoOperacion.DELETE.value, all_records=True)
        self.session.execute(query)
        logger.info(f"Datos eliminados de la tabla {tabla}")

    def eliminar_registro_tabla1(self, pelicula_categoria: str, pelicula_nombre: str):
        """
            Descripción: Función para eliminar un registro de la tabla 1
        """
        query = queryStringTemplates(
            'Tabla1', [], TipoOperacion.DELETE.value,
            where_columns=['pelicula_categoria', 'pelicula_nombre'])

        logger.info(f"Delete query: {query}")
        _delete_statement = self.session.prepare(query)
        self.session.execute(_delete_statement, [pelicula_categoria, pelicula_nombre])
        logger.info(
            f"Registro con categoría {pelicula_categoria} y "
            f"nombre {pelicula_nombre} eliminado de la tabla Tabla1")

    def eliminar_registro_tabla6(self, pelicula_categoria: str, pelicula_actores: str):
        """
            Descripción: Función para eliminar un registro de la tabla 6
        """
        query = queryStringTemplates(
            'Tabla6', [], TipoOperacion.DELETE.value,
            where_columns=['pelicula_categoria', 'pelicula_actor'])

        logger.info(f"Delete query: {query}")
        _delete_statement = self.session.prepare(query)

        for pelicula_actor in pelicula_actores:
            self.session.execute(_delete_statement, [pelicula_categoria, pelicula_actor])
            logger.info(
                f"Registro con categoría {pelicula_categoria} y "
                f"actor {pelicula_actor} eliminado de la tabla Tabla6")

    def eliminar_relacion_tarjeta_reservacion(self, **kwargs):
        """
            Descripción: Función para eliminar una relación de la tabla 5
        """

        tarjeta_nro = pedir_dato('tarjeta_nro', 'número', 'Tarjeta', **kwargs)
        tarjeta_nro = int(tarjeta_nro)
        reservacion_nro = pedir_dato('reservacion_nro', 'número de reservación', 'Reservación', **kwargs)

        _select_instance = Selects(self.session)
        _tarjeta = _select_instance.selectDatosTarjeta(tarjeta_nro=tarjeta_nro)

        self.eliminar_registro_tabla5(
            tarjeta_banco=_tarjeta.banco, tarjeta_nro=tarjeta_nro, reservacion_nro=reservacion_nro)

    def eliminar_registro_tabla5(self, tarjeta_banco: str, tarjeta_nro: int, reservacion_nro: str):
        """
            Descripción: Función para eliminar un registro de la tabla 5
        """
        query = queryStringTemplates(
            'Tabla5', [], TipoOperacion.DELETE.value,
            where_columns=['tarjeta_banco', 'tarjeta_nro', 'reservacion_nro'])

        logger.info(f"Delete query: {query}")
        _delete_statement = self.session.prepare(query)
        self.session.execute(_delete_statement, [tarjeta_banco, tarjeta_nro, reservacion_nro])
        logger.info(
            f"Registro con banco {tarjeta_banco}, número {tarjeta_nro} y "
            f"reservación {reservacion_nro} eliminado de la tabla Tabla5")
