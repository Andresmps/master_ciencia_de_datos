# Importamos la líbreria necesaria
import logging

from cassandra.cluster import Cluster

from crud.inserts import Inserts
from crud.selects import Selects
from crud.updates import Updates
from crud.deletes import Deletes
from crud.utils import Logging

logging.basicConfig(
    format=Logging.MSG_FORMAT.value,
    datefmt=Logging.DATETIME_FORMAT.value, level=logging.INFO,
)

logger = logging.getLogger(Logging.MENU_LOGGER.value)

def connectCassandra():
    """
        Descripción: Función para conectar a la base de datos de Cassandra
    """
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect('camilomartinez')
    return session

def welcomeMessage():
    welcome_message = """\n
-------------------------------------------------------------------------------------------
    *** Bienvenido al CRUD del Sistema de Almacenamiento de Datos con Cassandra ***"""

    print(welcome_message)

def mensajeMenu():
    """
        Descripción: Función para generar un mensaje de bienvenida
    """

    menu_mensaje =  """
-------------------------------------------------------------------------------------------
    Introduzca un número para ejecutar una de las siguientes operaciones:

    Insertar datos:
    \t1. Insertar paciente
    \t2. Insertar médico

    Selección de datos:
    \t10. Seleccionar datos de paciente
    \t11. Seleccionar datos de médico

    Actualizar datos:
    \t40. Actualizar dirección de paciente

    Cerrar aplicación:
    \t0. Cerrar aplicación
-------------------------------------------------------------------------------------------
"""
    print(menu_mensaje)

def menu():
    """
        Descripción: Función para mostrar el menú de opciones
    """

    session = connectCassandra()
    _insert_instance = Inserts(session=session)
    _select_instance = Selects(session=session)
    _update_instance = Updates(session=session)
    _delete_instance = Deletes(session=session)
    numero = -1

    welcomeMessage()
    # Sigue pidiendo operaciones hasta que se introduzca 0
    while (numero != 0):
        mensajeMenu()

        numero = int(input("Opción: ")) # Pedimos numero al usuario
        if numero == 1:
            _insert_instance.insertar_paciente()
        elif numero == 2:
            _insert_instance.insertar_medico()

        elif numero == 10:
            _select_instance.selectDatosPaciente()
        elif numero == 11:
            _select_instance.selectDatosMedico()

        elif numero == 40:
            _update_instance.actualizarDireccionPaciente()

        # elif numero == 50:
        #     _delete_instance.eliminar_relacion_

        # elif numero == 60:
        #     cargar_tablas(session)
        # elif numero == 61:
        #     eliminar_datos(session)

        elif numero == 0:
            print ("Cerrando aplicación")
            session.shutdown()
            break
        else:
            print ("Número incorrecto")



if __name__ == "__main__":
    menu()