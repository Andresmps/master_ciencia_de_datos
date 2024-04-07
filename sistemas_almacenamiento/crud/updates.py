import logging

from dataclasses import dataclass

from .clases_tablas import Pelicula
from .utils import TipoOperacion, queryStringTemplates, Logging

from .selects import Selects
from .inserts import Inserts
from .deletes import Deletes

logging.basicConfig(
    format=Logging.MSG_FORMAT.value,
    datefmt=Logging.DATETIME_FORMAT.value, level=logging.INFO,
)

logger = logging.getLogger(Logging.UPDATES_LOGGER.value)

@dataclass
class Updates:
    session: object

    def actualizarCategoriaPelicula(
            self, pelicula_nombre: str = None, pelicula_nueva_categoria: str = None, **kwargs):
        """
            Descripción: Función para actualizar la categoría de una película
        """
        _select_instance = Selects(self.session)
        _insert_instance = Inserts(self.session)
        _delete_instance = Deletes(self.session)

        pelicula_nombre = \
            input('Ingrese el nombre de la película: ')\
            if pelicula_nombre is None else pelicula_nombre

        pelicula_nueva_categoria = \
            input('Ingrese la nueva categoría de la película: ')\
            if pelicula_nueva_categoria is None else pelicula_nueva_categoria

        _pelicula = _select_instance.selectDatosPelicula(pelicula_nombre=pelicula_nombre)

        if _pelicula is None:
            logger.error(f'La película {pelicula_nombre} no existe en la base de datos.')
            return

        _categoria = _pelicula.categoria
        _actores = _pelicula.actores

        _insert_instance.insertar_tabla1(
            categoria=pelicula_nueva_categoria, nombre=pelicula_nombre, actores=_actores)

        _delete_instance.eliminar_registro_tabla1(
            pelicula_nombre=pelicula_nombre, pelicula_categoria=_categoria)

        _insert_instance.insertar_tabla6(
            categoria=pelicula_nueva_categoria, nombre=pelicula_nombre, actores=_actores)

        _delete_instance.eliminar_registro_tabla6(
            pelicula_categoria=_categoria, pelicula_actores=_actores)

        self.actualizarSoportePelicula(
            pelicula_nombre=pelicula_nombre, pelicula_nueva_categoria=pelicula_nueva_categoria)

    def actualizarSoportePelicula(
            self, pelicula_nombre: str = None, pelicula_nueva_categoria: str = None):
        """
            Descripción: Función para actualizar la categoría de una película
        """
        _query_update_soporte_pelicula = queryStringTemplates(
            tabla='SoportePelicula', columnas=[], tipo_operacion=TipoOperacion.UPDATE.value,
            where_columns=['pelicula_nombre'], update_column='pelicula_categoria',
            update_value=pelicula_nueva_categoria
        )

        logger.info(f'Actualizando la categoría de la película {pelicula_nombre} a {pelicula_nueva_categoria}.')
        logger.info(f'Query: {_query_update_soporte_pelicula}')
        _update_statement = self.session.prepare(_query_update_soporte_pelicula)
        self.session.execute(_update_statement, [pelicula_nombre])
        logger.info(f'Actualización de la categoría de la película {pelicula_nombre} en la tabla SoportePelicula.')
