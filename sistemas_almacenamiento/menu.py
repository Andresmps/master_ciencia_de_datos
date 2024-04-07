# Importamos la líbreria necesaria
import logging
import streamlit as st

from cassandra.cluster import Cluster

from crud.inserts import Inserts
from crud.selects import Selects
from crud.updates import Updates
from crud.deletes import Deletes
from crud.utils import Logging
from crud.precarga_datos import eliminar_datos, cargar_tablas

logging.basicConfig(
    format=Logging.MSG_FORMAT.value,
    datefmt=Logging.DATETIME_FORMAT.value, level=logging.INFO,
)

logger = logging.getLogger(Logging.MENU_LOGGER.value)

@st.cache_resource()
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
    \t1. Insertar un Usuario
    \t2. Insertar una Película
    \t3. Insertar una Ciudad
    \t4. Insertar un Cine
    \t5. Insertar una Sala
    \t6. Insertar una Función
    \t7. Insertar una Tarjeta
    \t8. Insertar un Tipo de Boleto
    \t9. Insertar una Reservación


    Consultar datos:
    \t10. Seleccionar datos de usuario, dado su dni
    \t11. Seleccionar datos de película, dado su nombre
    \t12. Seleccionar datos de ciudad, dado su nombre
    \t13. Seleccionar datos de cine, dado su id
    \t14. Seleccionar datos de sala, dado su nombre
    \t15. Seleccionar datos de película-función, dado su id
    \t16. Seleccionar datos de tarjeta, dado su id
    \t17. Seleccionar datos de tipo boleto, dado su id
    \t18. Seleccionar datos de reservación, dado su id

    Mostrar todos los datos:
    \t20. Mostrar datos de usuarios
    \t21. Mostrar datos de películas
    \t22. Mostrar datos de ciudades
    \t23. Mostrar datos de cines
    \t24. Mostrar datos de salas
    \t25. Mostrar datos de películas-funciones
    \t26. Mostrar datos de tarjetas
    \t27. Mostrar datos de tipos de boletos
    \t28. Mostrar datos de reservaciones

    Mostrar datos tablas:
    \t30. Mostrar datos de tabla 1
    \t31. Mostrar datos de tabla 2
    \t32. Mostrar datos de tabla 3
    \t33. Mostrar datos de tabla 4
    \t34. Mostrar datos de tabla 5
    \t35. Mostrar datos de tabla 6
    \t36. Mostrar datos de tabla 7
    \t37. Mostrar datos de tabla 8

    Actualizar datos:
    \t40. Actualizar categoría de película

    Eliminar datos:
    \t50. Eliminar relación tarjeta-reservación

    Precarga de datos:
    \t60 Cargo datos de prueba
    \t61 Eliminar todos los datos de las tablas

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
            _insert_instance.insertar_usuario()
        elif numero == 2:
            _insert_instance.insertar_pelicula()
        elif numero == 3:
            _insert_instance.insertar_ciudad_adquirir_datos()
        elif numero == 4:
            _insert_instance.insertar_cine()
        elif numero == 5:
            _insert_instance.insertar_sala()
        elif numero == 6:
            _insert_instance.insertar_funcion()
        elif numero == 7:
            _insert_instance.insertar_tarjeta()
        elif numero == 8:
            _insert_instance.insertar_tipo_boleto()
        elif numero == 9:
            _insert_instance.insertar_reservacion()

        elif numero == 10:
            _select_instance.selectDatosUsuario()
        elif numero == 11:
            _select_instance.selectDatosPelicula()
        elif numero == 12:
            _select_instance.selectDatosCiudad()
        elif numero == 13:
            _select_instance.selectDatosCine()
        elif numero == 14:
            _select_instance.selectDatosSala()
        elif numero == 15:
            _select_instance.selectDatosPeliculaFuncion()
        elif numero == 16:
            _select_instance.selectDatosTarjeta()
        elif numero == 17:
            _select_instance.selectDatosTipoBoleto()
        elif numero == 18:
            _select_instance.selectDatosReservacion()

        elif numero == 20:
            _select_instance.mostrarDatosUsuario()
        elif numero == 21:
            _select_instance.mostrarDatosPelicula()
        elif numero == 22:
            _select_instance.mostrarDatosCiudad()
        elif numero == 23:
            _select_instance.mostrarDatosCine()
        elif numero == 24:
            _select_instance.mostrarDatosSala()
        elif numero == 25:
            _select_instance.mostrarDatosPeliculaFuncion()
        elif numero == 26:
            _select_instance.mostrarDatosTarjeta()
        elif numero == 27:
            _select_instance.mostrarDatosTipoBoleto()
        elif numero == 28:
            _select_instance.mostrarDatosReservacion()

        elif numero == 30:
            _select_instance.mostrarDatosTabla1()
        elif numero == 31:
            _select_instance.mostrarDatosTabla2()
        elif numero == 32:
            _select_instance.mostrarDatosTabla3()
        elif numero == 33:
            _select_instance.mostrarDatosTabla4()
        elif numero == 34:
            _select_instance.mostrarDatosTabla5()
        elif numero == 35:
            _select_instance.mostrarDatosTabla6()
        elif numero == 36:
            _select_instance.mostrarDatosTabla7()
        elif numero == 37:
            _select_instance.mostrarDatosTabla8()

        elif numero == 40:
            _update_instance.actualizarCategoriaPelicula()

        elif numero == 50:
            _delete_instance.eliminar_relacion_tarjeta_reservacion()

        elif numero == 60:
            cargar_tablas(session)
        elif numero == 61:
            eliminar_datos(session)

        elif numero == 0:
            print ("Cerrando aplicación")
            session.shutdown()
            break
        else:
            print ("Número incorrecto")



if __name__ == "__main__":
    menu()