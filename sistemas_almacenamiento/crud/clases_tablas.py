import datetime

from dataclasses import dataclass

# Creación de la entidad Película - SoportePelicula
@dataclass
class Pelicula:
    IdNombrePelicula: str
    categoria: str
    actores: set

    def __str__(self):
        return \
            f'Nombre Pelicula: {self.IdNombrePelicula}, ' +\
            f'Categoría: {self.categoria}, Actores: {self.actores}'

    def __dict__(self):
        return {
            'IdNombrePelicula': self.IdNombrePelicula,
            'categoria': self.categoria,
            'actores': self.actores
        }

# Creación de la entidad Usuario
@dataclass
class Usuario:
    dni: str
    nombre: str
    tlfs: set

    def __str__(self):
        return f'DNI: {self.dni}, Nombre: {self.nombre}, Teléfonos: {self.tlfs}'

    def __dict__(self):
        return {
            'dni': self.dni,
            'nombre': self.nombre,
            'telefonos': self.tlfs
        }

# Creación de la entidad Tipo Boleto
@dataclass
class TipoBoleto:
    IdNombreTipoBoleto: str
    descuento: int

    def __str__(self):
        return f'Tipo boleto: {self.IdNombreTipoBoleto}, Descuento: {self.descuento}'

    def __dict__(self):
        return {
            'IdNombreTipoBoleto': self.IdNombreTipoBoleto,
            'descuento': self.descuento
        }

# Creación de la entidad Reservación
@dataclass
class Reservacion:
    IdNroReservacion: str
    confirmado: bool
    IdFechaHoraFuncion: datetime
    IdPeliculaNombre: str

    def __str__(self):
        return f'Número Reserva: {self.IdNroReservacion}, Confirmado: {self.confirmado}, Fecha Función: {self.IdFechaHoraFuncion}, Película: {self.IdPeliculaNombre}'

    def __dict__(self):
        return {
            'IdNroReservacion': self.IdNroReservacion,
            'confirmado': self.confirmado,
            'IdFechaHoraFuncion': self.IdFechaHoraFuncion,
            'IdPeliculaNombre': self.IdPeliculaNombre
        }

# Creación de la entidad Ciudad
@dataclass
class Ciudad:
    IdNombreCiudad: str
    provincia: str
    comunidad_autonoma: str

    def __str__(self):
        return f'Nombre Ciudad: {self.IdNombreCiudad}, Provincia: {self.provincia}, Comunidad Autónoma: {self.comunidad_autonoma}'

    def __dict__(self):
        return {
            'IdNombreCiudad': self.IdNombreCiudad,
            'provincia': self.provincia,
            'comunidad_autonoma': self.comunidad_autonoma
        }

# Creación de la entidad Cine - SoporteCine
@dataclass
class Cine:
    IdCine: str
    nombre: str
    ubicacion: str

    def __str__(self):
        return f'ID Cine: {self.IdCine}, Nombre: {self.nombre}, Ubicación: {self.ubicacion}'

    def __dict__(self):
        return {
            'IdCine': self.IdCine,
            'nombre': self.nombre,
            'ubicacion': self.ubicacion
        }

# Creación de la entidad Sala
@dataclass
class Sala:
    IdNroSala: int
    capacidad: str

    def __str__(self):
        return f'Número Sala: {self.IdNroSala}, Capacidad: {self.capacidad}'

    def __dict__(self):
        return {
            'IdNroSala': self.IdNroSala,
            'capacidad': self.capacidad
        }

# Creación de la entidad Tarjeta
@dataclass
class Tarjeta:
    IdNroTarjeta: int
    fecha: str
    banco: str

    def __str__(self):
        return f'Número Tarjeta: {self.IdNroTarjeta}, Fecha: {self.fecha}, Banco: {self.banco}'

    def __dict__(self):
        return {
            'IdNroTarjeta': self.IdNroTarjeta,
            'fecha': self.fecha,
            'banco': self.banco
        }

# Creación de la relación CiudadCine
@dataclass
class CiudadCine:
    IdCine: str
    IdNombreCiudad: str

    def __str__(self):
        return f'ID Cine: {self.IdCine}, Ciudad: {self.IdNombreCiudad}'

    def __dict__(self):
        return {
            'IdCine': self.IdCine,
            'IdNombreCiudad': self.IdNombreCiudad
        }

# Creación de la relación CineSala
@dataclass
class CineSala:
    IdCine: str
    IdNroSala: str

    def __str__(self):
        return f'ID Cine: {self.IdCine}, Número Sala: {self.IdNroSala}'

    def __dict__(self):
        return {
            'IdCine': self.IdCine,
            'IdNroSala': self.IdNroSala
        }

# Creación de la relación UsuarioReservación
@dataclass
class Reserva:
    dni: str
    IdNroReservacion: str

    def __str__(self):
        return f'DNI: {self.dni}, Número Reserva: {self.IdNroReservacion}'

    def __dict__(self):
        return {
            'dni': self.dni,
            'IdNroReservacion': self.IdNroReservacion
        }

# Creación de la relación ReservaciónTipoBoleto
@dataclass
class Compra:
    IdNroReservacion: str
    IdNombreTipoBoleto: str
    nro_boletos: int

    def __str__(self):
        return f'Número Reserva: {self.IdNroReservacion}, Tipo Boleto: {self.IdNombreTipoBoleto}, Boletos: {self.nro_boletos}'

    def __dict__(self):
        return {
            'IdNroReservacion': self.IdNroReservacion,
            'IdNombreTipoBoleto': self.IdNombreTipoBoleto,
            'nro_boletos': self.nro_boletos
        }

# Creación de la relación FunciónPelicula
@dataclass
class PeliculaFuncion:
    IdFechaHoraFuncion: datetime
    IdNombrePelicula: str
    PorcentajeOcupacion: str

    def __str__(self):
        return f'Fecha Función: {self.IdFechaHoraFuncion}, Nombre Película: {self.IdNombrePelicula}, Porcentaje Ocupación: {self.PorcentajeOcupacion}'

    def __dict__(self):
        return {
            'IdFechaHoraFuncion': self.IdFechaHoraFuncion,
            'IdNombrePelicula': self.IdNombrePelicula,
            'PorcentajeOcupacion': self.PorcentajeOcupacion
        }









# --- Opcionales --- #
# Creación de la relación FunciónTipoBoleto
# @dataclass
# class Asocia:
#     IdFechaHoraFuncion: str
#     IdNombreTipoBoleto: str

#     def __str__(self):
#         return f'Fecha Función: {self.IdFechaHoraFuncion}, Tipo Boleto: {self.IdNombreTipoBoleto}'

#     def __dict__(self):
#         return {
#             'IdFechaHoraFuncion': self.IdFechaHoraFuncion,
#             'IdNombreTipoBoleto': self.IdNombreTipoBoleto
#         }

# # Creación de la relación FunciónReservación
# @dataclass
# class FuncionReservacion:
#     IdFechaHoraFuncion: str
#     IdNroReservacion: str

#     def __str__(self):
#         return f'Fecha Función: {self.IdFechaHoraFuncion}, Número Reserva: {self.IdNroReservacion}'

#     def __dict__(self):
#         return {
#             'IdFechaHoraFuncion': self.IdFechaHoraFuncion,
#             'IdNroReservacion': self.IdNroReservacion
#         }

# # Creación de la relación PelículaReservación
# @dataclass
# class PeliculaReservacion:
#     IdNombrePelicula: str
#     IdNroReservacion: str

#     def __str__(self):
#         return f'Nombre Película: {self.IdNombrePelicula}, Número Reserva: {self.IdNroReservacion}'

#     def __dict__(self):
#         return {
#             'IdNombrePelicula': self.IdNombrePelicula,
#             'IdNroReservacion': self.IdNroReservacion
#         }
