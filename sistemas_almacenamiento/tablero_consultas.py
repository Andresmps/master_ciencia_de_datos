# Importamos la líbreria necesaria
import logging
import streamlit as st

from cassandra.cluster import Cluster
from datetime import datetime

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


if __name__ == "__main__":
    _session = connectCassandra()
    _select_instance = Selects(session=_session)
    _insert_instance = Inserts(session=_session)
    _update_instance = Updates(session=_session)
    _delete_instance = Deletes(session=_session)

    opciones = ['Inicio', 'Consultas', 'Inserciones', 'Actualizaciones', 'Eliminaciones']
    opcion_tabla = st.sidebar.selectbox(
        'Seleccione la operación a realizar:', opciones,
        index=opciones.index(st.session_state.opcion_tabla))

    if 'opcion_tabla' not in st.session_state:
        st.session_state.opcion_tabla = 'Inicio'

    if opcion_tabla == 'Inicio':
        st.title('Sistema de Almacenamiento de Datos con Cassandra')
        st.subheader('Actividad 2 - Sistemas de Almacenamiento de Datos')

        st.text('En esta sección se presentan las operaciones CRUD para las tablas de la base de datos.')
        st.text('Seleccione una de las opciones del menú lateral para continuar.')

        # --------------------------------
        st.markdown('---')
        st.text('Existen datos sinteticos que se pueden cargar para realizar pruebas')
        st.text('También se puede hacer una limpieza de los datos en las tablas.')
        st.markdown('---')
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Cargar tablas de prueba'):
                cargar_tablas(_session)
        with col2:
            if st.button('Eliminar datos de todas las tablas'):
                eliminar_datos(_session)
        st.markdown('---')

        st.text('Autor: Camilo Martinez')
        st.text('Año: 2024')

    elif opcion_tabla == 'Consultas':
        st.title('Consulta de Datos')
        st.subheader('Actividad 2 - Sistemas de Almacenamiento de Datos')
        st.text('En esta sección se presentan las consultas para las tablas de la base de datos.')

        # --------------------------------
        st.markdown('---')
        st.text('Existen datos sinteticos que se pueden cargar para realizar pruebas')
        st.text('También se puede hacer una limpieza de los datos en las tablas.')
        st.markdown('---')
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Cargar tablas de prueba'):
                cargar_tablas(_session)
        with col2:
            if st.button('Eliminar datos de todas las tablas'):
                eliminar_datos(_session)
        st.markdown('---')

        # --------------------------------
        st.subheader('Consulta para Tabla1 - Películas por Categoría')
        categoria = st.text_input('Categoría de la Película:', value='Todos los públicos')
        if st.button('Consultar Tabla1'):
            df = _select_instance.selectDatosTabla1(categoria)
            st.dataframe(df, width=800)

        # ------------------------------
        st.subheader('Consulta para Tabla2 - Reservaciones por Usuario')
        dni = st.text_input('DNI del Usuario:', value='30989073')
        if st.button('Consultar Tabla2'):
            df = _select_instance.selectDatosTabla2(dni)
            st.dataframe(df, width=800)

        # ------------------------------
        st.subheader('Consulta para Tabla3 - Salas por Cine')
        nombre_cine = st.text_input('Nombre del Cine:', value='Cinepolis Luna')
        if st.button('Consultar Tabla3'):
            df = _select_instance.selectDatosTabla3(nombre_cine)
            st.dataframe(df, width=800)

        # ------------------------------
        st.subheader('Consulta para Tabla4 - Conteo de reservaciones por usuario')
        dni = st.text_input('DNI del Usuario: ', value='30989073')
        if st.button('Consultar Tabla4'):
            df = _select_instance.selectDatosTabla4(dni)
            st.dataframe(df, width=800)

        # ------------------------------
        st.subheader('Consulta para Tabla5 - Reservaciones por Banco de la Tarjeta')
        tarjeta_banco = st.text_input('Nombre del Banco de la Tarjeta:', value='Banco Solar')
        if st.button('Consultar Tabla5'):
            df = _select_instance.selectDatosTabla5(tarjeta_banco)
            st.dataframe(df, width=800)

        # ------------------------------
        st.subheader('Consulta para Tabla6 - Películas por Categoría (Optimizado por autor)')
        categoria = st.text_input('Categoría de la Película: ', value='Todos los públicos')
        actor = st.text_input('Autor de la Película: ', value='Mario Casas')
        if st.button('Consultar Tabla6'):
            df = _select_instance.selectDatosTabla6(categoria, actor)
            st.dataframe(df, width=800)

        # ------------------------------
        st.subheader('Consulta para Tabla7 - Usuarios por número de teléfono')
        telefono = st.text_input('Número de Teléfono:', value='600699920')
        if st.button('Consultar Tabla7'):
            df = _select_instance.selectDatosTabla7(telefono)
            st.dataframe(df, width=800)

        # ------------------------------
        st.subheader('Consulta para Tabla8 - Funciones por Ciudad')
        nombre = st.text_input('Nombre de la Ciudad:', value='Nueva Esperanza')
        if st.button('Consultar Tabla8'):
            df = _select_instance.selectDatosTabla8(nombre)
            st.dataframe(df, width=800)

    elif opcion_tabla == 'Inserciones':
        st.title('Inserción de Datos')
        st.subheader('Actividad 2 - Sistemas de Almacenamiento de Datos')
        st.text('En esta sección se presentan las inserciones para las tablas de la base de datos.')

        # --------------------------------
        st.markdown('---')
        st.text('Existen datos sinteticos que se pueden cargar para realizar pruebas')
        st.text('También se puede hacer una limpieza de los datos en las tablas.')
        st.markdown('---')
        col1, col2 = st.columns(2)  # Crea dos columnas
        with col1:
            if st.button('Cargar tablas de prueba'):
                cargar_tablas(_session)
        with col2:
            if st.button('Eliminar datos de todas las tablas'):
                eliminar_datos(_session)
        st.markdown('---')

        ciudades = _select_instance.mostrarDatosCiudad()
        ciudades_nombre = [ciudad.IdNombreCiudad for ciudad in ciudades] if ciudades else []
        # st.cache_data(ciudades_nombre)

        cines = _select_instance.mostrarDatosCine()
        cines_ids = [cine.IdCine for cine in cines] if cines else []
        # st.cache_data(cines_ids)

        salas = _select_instance.mostrarDatosSala()
        salas_nros = [sala.IdNroSala for sala in salas] if salas else []
        # st.cache_data(salas_nros)

        tipos_boletos = _select_instance.mostrarDatosTipoBoleto()
        tipos_boletos_nombres = [tipo.IdNombreTipoBoleto for tipo in tipos_boletos] if tipos_boletos else []
        # st.cache_data(tipos_boletos_nombres)

        funciones = _select_instance.mostrarDatosPeliculaFuncion()
        funciones_ids = [funcion.IdFechaHoraFuncion for funcion in funciones] if funciones else []
        # st.cache_data(funciones_ids)

        usuarios = _select_instance.mostrarDatosUsuario()
        usuarios_dni = {usuario.nombre: usuario.dni for usuario in usuarios} if usuarios else {}
        # st.cache_data(usuarios_dni)

        tarjetas = _select_instance.mostrarDatosTarjeta()
        tarjetas_nros = [tarjeta.IdNroTarjeta for tarjeta in tarjetas]

        st.subheader('Insertar Película')
        nombre_pelicula = st.text_input('Nombre de la Película:', value='El Padrino')
        categoria_pelicula = st.text_input('Categoría de la Película:', value='Drama')
        actores = st.text_input('Actores de la Película:', value='Marlon Brando,Al Pacino')
        if st.button('Insertar Película'):
            _insert_instance.insertar_pelicula(
                nombre=nombre_pelicula, categoria=categoria_pelicula,
                actores=set(actores.split(',')))

        # ------------------------------
        st.subheader('Insertar Usuario')
        dni_usuario = st.text_input('DNI del Usuario:', value='30989073')
        nombre_usuario = st.text_input('Nombre del Usuario:', value='Camilo Martinez')
        telefonos_usuario = st.text_input('Teléfonos del Usuario: (telefono1,telefono2,...)', value='600699920')
        if st.button('Insertar Usuario'):
            _insert_instance.insertar_usuario(
                dni=dni_usuario, nombre=nombre_usuario,
                telefonos=set(telefonos_usuario.split(',')))

        # ------------------------------
        st.subheader('Insertar Ciudad')
        nombre_ciudad = st.text_input('Nombre de la Ciudad:', value='Nueva Esperanza')
        provincia_ciudad = st.text_input('Provincia de la Ciudad:', value='Córdoba')
        comunidad_ciudad = st.text_input('Comunidad de la Ciudad:', value='Andalucía')
        if st.button('Insertar Ciudad'):
            _insert_instance.insertar_ciudad(
                nombre=nombre_ciudad,
                provincia=provincia_ciudad,
                comunidad_autonoma=comunidad_ciudad)

        # ------------------------------
        st.subheader('Insertar Cine')
        id_cine = st.text_input('ID del Cine:', value='CIN-001')
        nombre_cine = st.text_input('Nombre del Cine:', value='Cinepolis Luna')
        ubicacion_cine = st.text_input('Ubicación del Cine:', value='Calle 123')

        ciudad_nombre = st.selectbox('Ciudad del Cine:', ciudades_nombre)

        if st.button('Insertar Cine'):
            _insert_instance.insertar_cine(
                id=id_cine, nombre=nombre_cine,
                ubicacion=ubicacion_cine, ciudad_nombre=ciudad_nombre)

        # ------------------------------
        st.subheader('Insertar Sala')
        nro_salas = st.text_input('Número de Sala:', value=5)
        capacidad_sala = st.text_input('Capacidad de la Sala:', value='100')

        cine_id = st.selectbox('ID del Cine:', cines_ids)

        if st.button('Insertar Sala'):
            _insert_instance.insertar_sala(
                IdNroSala=nro_salas, capacidad=capacidad_sala, cine_id=cine_id)

        # ------------------------------
        st.subheader('Insertar Función')
        hora_funcion = st.text_input('Hora de la Función: (Formato de fecha y hora: YYYYMMDD_HHMM. Ejemplo: 20210930_1500)', value='20221010_1200')
        nombre_pelicula = st.text_input('Nombre de la Película: ', value='El Padrino')

        sala_nro = st.selectbox('Número de Sala:', salas_nros)
        if st.button('Insertar Función'):
            _insert_instance.insertar_funcion(
                IdFechaHoraFuncion=hora_funcion, IdNombrePelicula=nombre_pelicula, sala_nro=sala_nro)

        # ------------------------------
        st.subheader('Insertar Tarjeta de Crédito')
        nro_tarjeta = st.text_input('Número de la Tarjeta:', value=123456789)
        fecha_vencimiento = st.text_input('Fecha de Vencimiento: (Formato de fecha: YYYY-MM. Por ejemplo: 2021-09)', value='2023-12-31')
        banco_tarjeta = st.text_input('Banco de la Tarjeta:', value='Banco Solar')

        if st.button('Insertar Tarjeta'):
            _insert_instance.insertar_tarjeta(
                IdNroTarjeta=nro_tarjeta, fecha=fecha_vencimiento, banco=banco_tarjeta)

        # ------------------------------
        st.subheader('Insertar Tipo de Boleto')
        tipo_boleto = st.text_input('Tipo de Boleto:', value='Festivo')
        descuento_boleto = st.text_input('Descuento del Boleto:', value=10)

        if st.button('Insertar Tipo de Boleto'):
            _insert_instance.insertar_tipo_boleto(
                IdNombreTipoBoleto=tipo_boleto, descuento=descuento_boleto)

        # ------------------------------
        st.subheader('Insertar Reservación')
        nro_reservacion = st.text_input('Número de Reservación:', value="RES015")
        confirmacion_reservacion = st.text_input(
            'Confirmación de la Reservación:', value=True)

        dni_usuario = st.selectbox('Usuario: ', list(usuarios_dni.keys()))
        dni_usuario = usuarios_dni.get(dni_usuario)

        fecha_hora_funcion = st.selectbox('Fecha y Hora de la Función: ', funciones_ids)
        if fecha_hora_funcion is not None:
            fecha_hora_funcion = fecha_hora_funcion.strftime('%Y%m%d_%H%M')

        nro_tarjetas = st.multiselect('Números de la Tarjetas: ', tarjetas_nros)

        tipos_boletos = st.multiselect('Tipos de Boletos: ', tipos_boletos_nombres)
        tipos_boletos = {tipo: 1 for tipo in tipos_boletos}

        if st.button('Insertar Reservación'):
            _insert_instance.insertar_reservacion(
                IdNroReservacion=nro_reservacion, confirmado=confirmacion_reservacion,
                usuario_dni=dni_usuario, IdFechaHoraFuncion=fecha_hora_funcion,
                tarjetas=nro_tarjetas,
                tipos_boletas=tipos_boletos)
    elif opcion_tabla == "Actualizaciones":
        st.title('Actualización de Datos')
        st.subheader('Actividad 2 - Sistemas de Almacenamiento de Datos')
        st.text('En esta sección se presentan las actualizaciones para las tablas de la base de datos.')

        tabla1_datos = _select_instance.mostrarDatosTabla1()
        peliculas_dfs = [
            {
                'Nombre de la Película': _pelicula.pelicula_nombre,
                'Categoría': _pelicula.pelicula_categoria
            } for _pelicula in tabla1_datos
        ]
        _peliculas_nombres = [pelicula['Nombre de la Película'] for pelicula in peliculas_dfs]

        # --------------------------------
        st.markdown('---')
        st.text('Existen datos sinteticos que se pueden cargar para realizar pruebas')
        st.text('También se puede hacer una limpieza de los datos en las tablas.')
        st.markdown('---')
        col1, col2 = st.columns(2)  # Crea dos columnas
        with col1:
            if st.button('Cargar tablas de prueba'):
                cargar_tablas(_session)
        with col2:
            if st.button('Eliminar datos de todas las tablas'):
                eliminar_datos(_session)
        st.markdown('---')

        # --------------------------------

        st.subheader('Peliculas')

        # df = _select_instance.selectDatosTabla5(_tarjeta.banco)
        st.dataframe(peliculas_dfs, width=800)
        st.markdown('---')

        # --------------------------------
        st.subheader('Actualizar Categoria de Película')
        nombre_pelicula = st.selectbox('Nombre de la Película:', _peliculas_nombres)
        nueva_categoria = st.text_input('Nueva Categoría de la Película:', value='Drama')
        if st.button('Actualizar Categoría de Película'):
            _pelicula = _select_instance.selectDatosPelicula(pelicula_nombre=nombre_pelicula)

            st.text(f"\nTabla 1 - Antes de actualizar la categoría de la película:")
            st.markdown('---')
            df = _select_instance.selectDatosTabla1(_pelicula.categoria)
            st.dataframe(df, width=800)

            _update_instance.actualizarCategoriaPelicula(
                pelicula_nombre=nombre_pelicula, pelicula_nueva_categoria=nueva_categoria)

            st.text(f"Tabla 1 - Después de actualizar la categoría de la película:")
            st.markdown('---')
            df = _select_instance.selectDatosTabla1(nueva_categoria)
            st.dataframe(df, width=800)

    elif opcion_tabla == "Eliminaciones":
        st.title('Eliminación de Datos')
        st.subheader('Actividad 2 - Sistemas de Almacenamiento de Datos')
        st.text('En esta sección se presentan las eliminaciones para las tablas de la base de datos.')

        tarjetas = _select_instance.mostrarDatosTarjeta()
        tarjetas_nros = [tarjeta.IdNroTarjeta for tarjeta in tarjetas]

        reservaciones = _select_instance.mostrarDatosReservacion()
        reservaciones_nros = [reservacion.IdNroReservacion for reservacion in reservaciones]

        tabla5_datos = _select_instance.mostrarDatosTabla5()
        reservaciones_dfs = [
            {
                'Número de Reservación': reservacion.reservacion_nro,
                'Número de Tarjeta': str(reservacion.tarjeta_nro),
                'Banco de la Tarjeta': reservacion.tarjeta_banco
            } for reservacion in tabla5_datos
        ]

        # --------------------------------
        st.markdown('---')
        st.text('Existen datos sinteticos que se pueden cargar para realizar pruebas')
        st.text('También se puede hacer una limpieza de los datos en las tablas.')
        st.markdown('---')
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Cargar tablas de prueba'):
                cargar_tablas(_session)
        with col2:
            if st.button('Eliminar datos de todas las tablas'):
                eliminar_datos(_session)
        st.markdown('---')

        # --------------------------------
        st.subheader('Relacion tarjeta-reservación')

        # df = _select_instance.selectDatosTabla5(_tarjeta.banco)
        st.dataframe(reservaciones_dfs, width=800)
        st.markdown('---')

        st.subheader('Eliminar relacion tarjeta-reservación')
        nro_tarjeta = st.selectbox('Número de la Tarjeta:', tarjetas_nros)
        nro_reservacion = st.selectbox(
            'Número de la Reservación:', reservaciones_nros, index=reservaciones_nros.index('RES001'))
        if st.button('Eliminar relación Tarjeta-Reservación'):
            _tarjeta = _select_instance.selectDatosTarjeta(tarjeta_nro=nro_tarjeta)

            st.text(f"\nTabla 5 - Antes de eliminar la relación Tarjeta-Reservación:")
            st.markdown('---')
            df = _select_instance.selectDatosTabla5(_tarjeta.banco)
            st.dataframe(df, width=800)

            st.text(f"Tabla 5 - Después de eliminar la relación Tarjeta-Reservación:")
            st.markdown('---')
            _delete_instance.eliminar_relacion_tarjeta_reservacion(
                tarjeta_nro=nro_tarjeta, reservacion_nro=nro_reservacion)

            df = _select_instance.selectDatosTabla5(_tarjeta.banco)
            st.dataframe(df, width=800)
