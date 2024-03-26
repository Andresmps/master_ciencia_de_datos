# Importamos la líbreria necesaria
import datetime

from cassandra.cluster import Cluster
from dataclasses import dataclass
# Conexión a Cassandra

cluster = Cluster()
session = cluster.connect('camilomartinez')


# Creación de la clase Ciudad
@dataclass
class Ciudad:
    IdNombreCiudad: str
    provincia: str
    comunidad_autonoma: str

# Creación de la clase SoporteCine
@dataclass
class SoporteCine:
    IdCine: str
    nombre: str
    ubicacion: str
    IdNombreCiudad: str

# Creación de la clase Sala
@dataclass
class Sala:
    IdNroSala: str
    # capacidad: int
    IdCine: str

# Creación de la clase Película
@dataclass
class Pelicula:
    IdNombrePelicula: str
    categoria: str
    actores: str

# Creación de la clase Función
@dataclass
class Funcion:
    IdFechaHoraFuncion: str
    porcentaje_ocupacion: float
    IdNombrePelicula: str

#Creación de la clase Tipo Boleto
@dataclass
class TipoBoleto:
    IdNombreTipoBoleto: str
    descuento: float

# Creación de la clase Reservación
@dataclass
class Reservacion:
    IdNroReservacion: str
    confirmado: bool
    DNI: str

# Creación de la clase Usuario
@dataclass
class Usuario:
    DNI: str
    nombre: str
    tlfs: str

# Creación de la clase Tarjeta
@dataclass
class Tarjeta:
    IdNroTarjeta: str
    fecha: datetime.date
    banco: str

# Creación de la clase intermedia entre Función vs tipo de boleto
@dataclass
class FuncionTipoBoleto:
    IdFechaHoraFuncion: str
    IdNombreTipoBoleto: str

# Creación de la clase intermedia entre Funcion vs Reservacion
@dataclass
class FuncionReservacion:
    IdFechaHoraFuncion: str
    IdNroReservacion: str

# Creación de la clase intermedia entre Película y Reservación
@dataclass
class PeliculaReservacion:
    IdNombrePelicula: str
    IdNroReservacion: str

# Creación de la clase intermedia entre Tipo Boleto y Reservación
@dataclass
class TipoBoletoReservacion:
    IdNombreTipoBoleto: str
    IdNroReservacion: str

# Creación de la clase intermedia entre Reservación y Tarjeta
@dataclass
class ReservacionTarjeta:
    IdNroReservacion: str
    IdNroTarjeta: str
