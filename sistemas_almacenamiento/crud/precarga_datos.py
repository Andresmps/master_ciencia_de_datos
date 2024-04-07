import logging

from crud.inserts import Inserts
from crud.deletes import Deletes

peliculas = [
    {"nombre": "Voces Ocultas", "categoria": "Todos los públicos", "actores": {"María Valverde", "Daniel Grao"}},
    {"nombre": "El Último Viaje", "categoria": "Todos los públicos", "actores": {"Clara Lago", "Álex González"}},
    {"nombre": "Raíces Perdidas", "categoria": "Todos los públicos", "actores": {"Bárbara Lennie", "Eduard Fernández"}},
    {"nombre": "El Guardián Invisible", "categoria": "Drama", "actores": {"Martina García", "Antonio de la Torre", "Mario Casas"}},
    {"nombre": "Laberinto de Ilusiones", "categoria": "Suspense", "actores": {"Javier Gutiérrez", "Adriana Ugarte"}},
    {"nombre": "Miradas del Ayer", "categoria": "Todos los públicos", "actores": {"Blanca Suárez", "Mario Casas"}},
    {"nombre": "Desierto de Esperanzas", "categoria": "Todos los públicos", "actores": {"Penélope Cruz", "Luis Tosar"}},
    {"nombre": "Sonrisas de Papel", "categoria": "Comedia", "actores": {"Carmen Machi", "Paco León"}},
    {"nombre": "Caminos Cruzados", "categoria": "Acción", "actores": {"Rodrigo Sorogoyen", "Belén Cuesta", "Mario Casas"}},
    {"nombre": "Más Allá del Horizonte", "categoria": "Todos los públicos", "actores": {"Natalia de Molina", "Javier Bardem"}}
]

usuarios = [
    {'dni': '30989073', 'nombre': 'Daniel Gómez', 'telefonos': {'600699920', '693601870'}},
    {'dni': '90003479', 'nombre': 'Carlos Pérez', 'telefonos': {'649194738', '684957063'}},
    {'dni': '67958689', 'nombre': 'Carlos Gómez', 'telefonos': {'613035256', '641203820'}},
    {'dni': '46805707', 'nombre': 'María González', 'telefonos': {'601087597', '661169421'}},
    {'dni': '17365531', 'nombre': 'Juan Pérez', 'telefonos': {'611449818', '658784870'}},
    {'dni': '40744447', 'nombre': 'Sofía Martínez', 'telefonos': {'605578585', '614742565'}},
    {'dni': '14972145', 'nombre': 'David Sánchez', 'telefonos': {'684358968', '600699920'}},
    {'dni': '29507230', 'nombre': 'Daniel González', 'telefonos': {'647312434', '683125107'}},
    {'dni': '45442552', 'nombre': 'Marta Gómez', 'telefonos': {'600699920', '666380422'}},
    {'dni': '50272061', 'nombre': 'Lucía Fernández', 'telefonos': {'664713600', '681074323'}}
]

ciudades = [
    {"nombre": "Nueva Esperanza", "provincia": "Provincia Alfa", "comunidad_autonoma": "Comunidad Solar"},
    {"nombre": "Villa Sol", "provincia": "Provincia Beta", "comunidad_autonoma": "Comunidad Lunar"},
    {"nombre": "Ciudad Luz", "provincia": "Provincia Gamma", "comunidad_autonoma": "Comunidad Estelar"},
    {"nombre": "Puerto Sueños", "provincia": "Provincia Delta", "comunidad_autonoma": "Comunidad Galáctica"},
    {"nombre": "Oasis Verde", "provincia": "Provincia Epsilon", "comunidad_autonoma": "Comunidad Nebular"},
    {"nombre": "Valle Azul", "provincia": "Provincia Zeta", "comunidad_autonoma": "Comunidad Cósmica"},
    {"nombre": "Monte Alto", "provincia": "Provincia Eta", "comunidad_autonoma": "Comunidad Aurora"},
    {"nombre": "Río Tranquilo", "provincia": "Provincia Theta", "comunidad_autonoma": "Comunidad Vía Láctea"},
    {"nombre": "Costa Dorada", "provincia": "Provincia Iota", "comunidad_autonoma": "Comunidad Andromeda"},
    {"nombre": "Llanura Infinita", "provincia": "Provincia Kappa", "comunidad_autonoma": "Comunidad Cosmos"}
]

cines = [
    {"id": "CINE001", "nombre": "Cinemax Solar", "ubicacion": "Avenida Estrella 123", "ciudad_nombre": "Nueva Esperanza"},
    {"id": "CINE002", "nombre": "Cinepolis Luna", "ubicacion": "Boulevard Lunar 456", "ciudad_nombre": "Villa Sol"},
    {"id": "CINE003", "nombre": "Cineplanet Cosmos", "ubicacion": "Calle Cosmos 789", "ciudad_nombre": "Ciudad Luz"},
    {"id": "CINE004", "nombre": "Multicines Galaxia", "ubicacion": "Plaza Galáctica 101", "ciudad_nombre": "Puerto Sueños"},
    {"id": "CINE005", "nombre": "Cine Estelar", "ubicacion": "Avenida Nebulosa 202", "ciudad_nombre": "Oasis Verde"},
    {"id": "CINE006", "nombre": "Cineland Aurora", "ubicacion": "Calle Aurora 303", "ciudad_nombre": "Valle Azul"},
    {"id": "CINE007", "nombre": "Cinevia Láctea", "ubicacion": "Vía Láctea 404", "ciudad_nombre": "Nueva Esperanza"},
    {"id": "CINE008", "nombre": "Andrómeda Films", "ubicacion": "Sector Andromeda 505", "ciudad_nombre": "Río Tranquilo"},
    {"id": "CINE009", "nombre": "Cinema Nova", "ubicacion": "Avenida Nova 606", "ciudad_nombre": "Costa Dorada"},
    {"id": "CINE010", "nombre": "Estrellas del Cine", "ubicacion": "Calle Estrella 707", "ciudad_nombre": "Nueva Esperanza"}
]

salas = [
    {"IdNroSala": 1, "capacidad": "150 personas", "cine_id": "CINE001"},
    {"IdNroSala": 2, "capacidad": "200 personas", "cine_id": "CINE001"},
    {"IdNroSala": 3, "capacidad": "100 personas", "cine_id": "CINE002"},
    {"IdNroSala": 4, "capacidad": "120 personas", "cine_id": "CINE002"},
    {"IdNroSala": 5, "capacidad": "250 personas", "cine_id": "CINE003"},
    {"IdNroSala": 6, "capacidad": "300 personas", "cine_id": "CINE003"},
    {"IdNroSala": 7, "capacidad": "180 personas", "cine_id": "CINE004"},
    {"IdNroSala": 8, "capacidad": "220 personas", "cine_id": "CINE004"},
    {"IdNroSala": 9, "capacidad": "130 personas", "cine_id": "CINE005"},
    {"IdNroSala": 10, "capacidad": "160 personas", "cine_id": "CINE005"}
]

funciones = [
    {"IdFechaHoraFuncion": "20231005_1400", "IdNombrePelicula": "Voces Ocultas", "sala_nro": 1, "PorcentajeOcupacion": 75},
    {"IdFechaHoraFuncion": "20231005_1600", "IdNombrePelicula": "El Último Viaje", "sala_nro": 2, "PorcentajeOcupacion": 60},
    {"IdFechaHoraFuncion": "20231006_1400", "IdNombrePelicula": "Raíces Perdidas", "sala_nro": 3, "PorcentajeOcupacion": 80},
    {"IdFechaHoraFuncion": "20231006_1600", "IdNombrePelicula": "El Guardián Invisible", "sala_nro": 4, "PorcentajeOcupacion": 50},
    {"IdFechaHoraFuncion": "20231007_1400", "IdNombrePelicula": "Laberinto de Ilusiones", "sala_nro": 5, "PorcentajeOcupacion": 90},
    {"IdFechaHoraFuncion": "20231007_1600", "IdNombrePelicula": "Miradas del Ayer", "sala_nro": 6, "PorcentajeOcupacion": 65},
    {"IdFechaHoraFuncion": "20231008_1400", "IdNombrePelicula": "Desierto de Esperanzas", "sala_nro": 7, "PorcentajeOcupacion": 70},
    {"IdFechaHoraFuncion": "20231008_1600", "IdNombrePelicula": "Sonrisas de Papel", "sala_nro": 8, "PorcentajeOcupacion": 85},
    {"IdFechaHoraFuncion": "20231009_1400", "IdNombrePelicula": "Caminos Cruzados", "sala_nro": 9, "PorcentajeOcupacion": 55},
    {"IdFechaHoraFuncion": "20231009_1600", "IdNombrePelicula": "Más Allá del Horizonte", "sala_nro": 10, "PorcentajeOcupacion": 95}
]

tarjetas = [
    {"IdNroTarjeta": "4567891234567890", "fecha": "2023-01", "banco": "Banco Solar"},
    {"IdNroTarjeta": "1234567890123456", "fecha": "2023-02", "banco": "Banco Lunar"},
    {"IdNroTarjeta": "9876543210987654", "fecha": "2023-03", "banco": "Banco Galáctico"},
    {"IdNroTarjeta": "6543219876543210", "fecha": "2023-04", "banco": "Banco Estelar"},
    {"IdNroTarjeta": "3210987654321098", "fecha": "2023-05", "banco": "Banco de la Vía Láctea"},
    {"IdNroTarjeta": "7890123456789012", "fecha": "2023-06", "banco": "Banco Andromeda"},
    {"IdNroTarjeta": "5678901234567890", "fecha": "2023-07", "banco": "Banco Nebular"},
    {"IdNroTarjeta": "2345678901234567", "fecha": "2023-08", "banco": "Banco Cosmos"},
    {"IdNroTarjeta": "8901234567890123", "fecha": "2023-09", "banco": "Banco Aurora"},
    {"IdNroTarjeta": "4567890123456789", "fecha": "2023-10", "banco": "Banco Quantum"}
]

tipos_boletos = [
    {"IdNombreTipoBoleto": "General", "descuento": 0},
    {"IdNombreTipoBoleto": "Estudiante", "descuento": 15},
    {"IdNombreTipoBoleto": "Senior", "descuento": 20},
    {"IdNombreTipoBoleto": "Niño", "descuento": 10},
    {"IdNombreTipoBoleto": "Familia", "descuento": 25},
    {"IdNombreTipoBoleto": "Pareja", "descuento": 5},
    {"IdNombreTipoBoleto": "Madrugador", "descuento": 30},
    {"IdNombreTipoBoleto": "Noche", "descuento": 5},
    {"IdNombreTipoBoleto": "Fiesta", "descuento": 20},
    {"IdNombreTipoBoleto": "VIP", "descuento": 0}
]

reservaciones = [
    {"IdNroReservacion": "RES001", "confirmado": True, "usuario_dni": "30989073", "IdFechaHoraFuncion": "20231005_1400", "tarjetas": ["4567891234567890"], "tipos_boletas": {"General": 2}},
    {"IdNroReservacion": "RES002", "confirmado": False, "usuario_dni": "30989073", "IdFechaHoraFuncion": "20231005_1600", "tarjetas": ["1234567890123456"], "tipos_boletas": {"Estudiante": 1, "General": 1}},
    {"IdNroReservacion": "RES003", "confirmado": True, "usuario_dni": "67958689", "IdFechaHoraFuncion": "20231006_1400", "tarjetas": ["9876543210987654", "1234567890123456"], "tipos_boletas": {"Senior": 3}},
    {"IdNroReservacion": "RES004", "confirmado": True, "usuario_dni": "46805707", "IdFechaHoraFuncion": "20231006_1600", "tarjetas": ["6543219876543210"], "tipos_boletas": {"Niño": 2}},
    {"IdNroReservacion": "RES005", "confirmado": False, "usuario_dni": "17365531", "IdFechaHoraFuncion": "20231007_1400", "tarjetas": ["3210987654321098"], "tipos_boletas": {"Familia": 4}},
    {"IdNroReservacion": "RES006", "confirmado": True, "usuario_dni": "40744447", "IdFechaHoraFuncion": "20231007_1600", "tarjetas": ["7890123456789012"], "tipos_boletas": {"Pareja": 2}},
    {"IdNroReservacion": "RES007", "confirmado": True, "usuario_dni": "40744447", "IdFechaHoraFuncion": "20231008_1400", "tarjetas": ["5678901234567890"], "tipos_boletas": {"Madrugador": 3, "General": 1}},
    {"IdNroReservacion": "RES008", "confirmado": False, "usuario_dni": "30989073", "IdFechaHoraFuncion": "20231008_1600", "tarjetas": ["2345678901234567"], "tipos_boletas": {"Noche": 2}},
    {"IdNroReservacion": "RES009", "confirmado": True, "usuario_dni": "45442552", "IdFechaHoraFuncion": "20231009_1400", "tarjetas": ["8901234567890123"], "tipos_boletas": {"Fiesta": 2}},
    {"IdNroReservacion": "RES010", "confirmado": True, "usuario_dni": "46805707", "IdFechaHoraFuncion": "20231009_1600", "tarjetas": ["4567890123456789", "8901234567890123"], "tipos_boletas": {"VIP": 2, "General": 1}}
]


def cargar_tablas(_sesion):
    """
        Descripción: Función para cargar los datos de las tablas
    """

    _inserts = Inserts(_sesion)
    for _usuario in usuarios:
        logging.info(f'Insertando usuario: {_usuario}')
        _inserts.insertar_usuario(**_usuario)

    for _pelicula in peliculas:
        logging.info(f'Insertando película: {_pelicula}')
        _inserts.insertar_pelicula(**_pelicula)

    for _ciudad in ciudades:
        logging.info(f'Insertando ciudad: {_ciudad}')
        _inserts.insertar_ciudad_adquirir_datos(**_ciudad)

    for _cine in cines:
        logging.info(f'Insertando cine: {_cine}')
        _inserts.insertar_cine(**_cine)

    for _sala in salas:
        logging.info(f'Insertando sala: {_sala}')
        _inserts.insertar_sala(**_sala)

    for _funcion in funciones:
        logging.info(f'Insertando función: {_funcion}')
        _inserts.insertar_funcion(**_funcion)

    for _tarjeta in tarjetas:
        logging.info(f'Insertando tarjeta: {_tarjeta}')
        _inserts.insertar_tarjeta(**_tarjeta)

    for _tipo_boleto in tipos_boletos:
        logging.info(f'Insertando tipo boleto: {_tipo_boleto}')
        _inserts.insertar_tipo_boleto(**_tipo_boleto)

    for _reservacion in reservaciones:
        logging.info(f'Insertando reservación: {_reservacion}')
        _inserts.insertar_reservacion(**_reservacion)

def eliminar_datos(_sesion):
    """
        Descripción: Función para eliminar todos los datos de las tablas
    """
    _deletes = Deletes(_sesion)
    _deletes.eliminar_datos_todas_tables()
