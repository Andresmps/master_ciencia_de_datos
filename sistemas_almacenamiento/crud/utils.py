import logging

from enum import Enum

KEYSPACE = "camilomartinez"

class TipoOperacion(Enum):
    INSERT = "INSERT"
    SELECT = "SELECT"
    UPDATE = "UPDATE"
    DELETE = "DELETE"

class Logging(Enum):
    MSG_FORMAT = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    MENU_LOGGER = "Database Menu"
    SELECTS_LOGGER = "Database Selects"
    INSERTS_LOGGER = "Database Inserts"
    UPDATES_LOGGER = "Database Updates"
    DELETES_LOGGER = "Database Deletes"

def queryStringTemplates(
        tabla: str, columnas: list, tipo_operacion: str, **kwargs):
    """
        Descripción: Función para crear una cadena de texto con la consulta a realizar en Cassandra.
            Principalmente se utiliza para evitar errores de formato en las consultas.
    """
    query_template = None
    _columnas = '"' + '", "'.join(columnas) + '"' # Genera ("columna1", "columna2", ...)
    _values = ', '.join(['?' for _ in range(len(columnas))]) # Genera (?, ?, ?, ...)

    if tipo_operacion == TipoOperacion.INSERT.value:
        query_template = f'INSERT INTO "{KEYSPACE}"."{tabla}" ({_columnas}) VALUES ({_values})'
    elif tipo_operacion == TipoOperacion.SELECT.value:
        where_columns = kwargs.get('where_columns', [])
        where_columns = \
            ' and '.join([f"{_col} = ?" for _col in where_columns]) # Genera "columna1 = ? and columna2 = ?"

        # Si all_columns es True, se seleccionan todas las columnas
        _columnas = '*' if kwargs.get('all_columns', False) else _columnas

        # Si where_columns es None, se seleccionan todos los registros
        query_template = \
            f'SELECT {_columnas} FROM "{KEYSPACE}"."{tabla}"' if not where_columns else\
            f'SELECT {_columnas} FROM "{KEYSPACE}"."{tabla}" WHERE {where_columns}'

    elif tipo_operacion == TipoOperacion.UPDATE.value:
        where_columns = kwargs.get('where_columns', [])
        where_columns = \
            ' and '.join([f"{_col} = ?" for _col in where_columns]) # Genera "columna1 = ? and columna2 = ?"

        # Identifica si la columna a actualizar es un contador, y que columna se va a actualizar
        _update_column = kwargs.get('update_column', None)
        _is_counter = kwargs.get('is_counter', False)
        _update_value = kwargs.get('update_value', None)

        if _is_counter:
            query_template = \
                f'UPDATE "{KEYSPACE}"."{tabla}" SET {_update_column} = {_update_column} + 1 WHERE {where_columns}'
        else:
            query_template = \
                f'UPDATE "{KEYSPACE}"."{tabla}" SET {_update_column} = \'{_update_value}\' WHERE {where_columns}'

    elif tipo_operacion == TipoOperacion.DELETE.value:
        where_columns = kwargs.get('where_columns', [])
        where_columns = \
            ' and '.join([f"{_col} = ?" for _col in where_columns]) # Genera "columna1 = ? and columna2 = ?"

        all_records = kwargs.get('all_records', False)

        if all_records:
            query_template = f'TRUNCATE "{KEYSPACE}"."{tabla}"'
        else:
            query_template = \
                f'DELETE FROM "{KEYSPACE}"."{tabla}" WHERE {where_columns}'

    return query_template

def pedir_dato(
        nombre_atributo: str, etiqueta_atributo: str, tabla: str, **kwargs):
    """
        Descripción: Función para pedir un dato al usuario
    """
    print(f"\n\tIngrese el/la {etiqueta_atributo} de {tabla}: ", end='')
    dato = input()\
        if kwargs.get(nombre_atributo) is None\
        else kwargs[nombre_atributo]
    return dato

def pedir_datos(nombre_atributo: str, etiqueta_atributo: str, tabla: str, **kwargs):
    """
        Descripción: Función para pedir un dato al usuario
    """
    datos = []

    print(
        f"\n\tIngresa los {nombre_atributo} de la tabla={tabla}."
        " (\".\" para detener la ejecución)\n"
    )
    if kwargs.get(nombre_atributo) is None:
        while True:
            dato = input(f"Introduzca el/la {etiqueta_atributo}: ")

            if dato == ".":
                break
            elif dato in datos or "".strip() == dato:
                logging.info(
                    f"El/La {etiqueta_atributo} ya está en la lista de {nombre_atributo}, inténtelo de nuevo.")
                continue
            else:
                datos.append(dato)
    else:
        datos = kwargs[nombre_atributo]

    return datos
