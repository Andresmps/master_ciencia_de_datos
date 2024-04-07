create keyspace camilomartinez with durable_writes = true and replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

use camilomartinez

-- Peliculas
CREATE TABLE camilomartinez."Tabla1"(
	pelicula_categoria text,
	pelicula_nombre text,
	pelicula_actores SET<text>,
	PRIMARY KEY (pelicula_categoria, pelicula_nombre)
) WITH CLUSTERING ORDER BY ( pelicula_nombre asc );

-- Reservas de un Usuario
CREATE TABLE camilomartinez."Tabla2"(
	usuario_dni text,
	reservacion_nro text,
	tipo_boleto_nombre text,
	PRIMARY KEY (usuario_dni, reservacion_nro)
) WITH CLUSTERING ORDER BY ( reservacion_nro ASC);


-- Salas de un cine
CREATE TABLE camilomartinez."Tabla3"(
	cine_nombre text,
	sala_nro int,
	PRIMARY KEY (cine_nombre, sala_nro)
) WITH CLUSTERING ORDER BY ( sala_nro ASC )

-- Conteo de reservaciones por usuario
CREATE TABLE camilomartinez."Tabla4"(
	usuario_dni text,
	reservacion_nro counter,
	PRIMARY KEY (usuario_dni)
)

-- Reservaciones a partir del banco de una tarjeta -> Relación n-m
CREATE TABLE camilomartinez."Tabla5"(
	tarjeta_banco text,
	tarjeta_nro bigint,
	reservacion_nro text,
	reservacion_confirmado boolean,
	PRIMARY KEY (tarjeta_banco, tarjeta_nro, reservacion_nro)
) WITH CLUSTERING ORDER BY ( tarjeta_nro ASC, reservacion_nro ASC );

-- Peliculas por categoria
CREATE TABLE camilomartinez."Tabla6"(
	pelicula_categoria text,
	pelicula_actor text,
	pelicula_nombre text,
	pelicula_actores set<text>,
	PRIMARY KEY ((pelicula_categoria, pelicula_actor), pelicula_nombre)
) WITH CLUSTERING ORDER BY ( pelicula_nombre ASC )


-- Usuarios por número de telefono
CREATE TABLE camilomartinez."Tabla7"(
	usuario_tlf text,
	usuario_dni text,
	usuario_nombre text,
	usuario_tlfs set<text>,
	PRIMARY KEY (usuario_tlf, usuario_dni)
) WITH CLUSTERING ORDER BY ( usuario_dni ASC );


-- Funciones por ciudad -> Ciudad / Cine / Sala / Función  - Pelicula / Funcion
CREATE TABLE camilomartinez."Tabla8"(
	ciudad_nombre text,
	pelicula_nombre text,
	funcion_fecha_hora timestamp,
	PRIMARY KEY ( ciudad_nombre, pelicula_nombre, funcion_fecha_hora)
) WITH CLUSTERING ORDER BY ( pelicula_nombre ASC, funcion_fecha_hora ASC );

-- Descripción: Dada una ciudad, obtener las funciones presentadas en esta.
-- Requerimientos: Una ciudad debe tener cines, un cine debe tener salas, una sala debe tener funciones. Además, debo considerar la relación Pelicula Funcion

CREATE TABLE camilomartinez."SoporteUsuario" (
	usuario_dni text,
	usuario_nombre text,
	usuario_tlfs SET<text>,
	PRIMARY KEY (usuario_dni)
);

CREATE TABLE camilomartinez."SoportePelicula"(
	pelicula_nombre text,
  	pelicula_categoria text,
	pelicula_actores set<text>,
	PRIMARY KEY (pelicula_nombre)
);


CREATE TABLE camilomartinez."SoporteCiudad"(
	ciudad_nombre text,
  	ciudad_provincia text,
	ciudad_comunidad_autonoma text,
	PRIMARY KEY (ciudad_nombre)
);

CREATE TABLE camilomartinez."SoporteSala"(
	sala_nro int,
  	capacidad text,
	PRIMARY KEY (sala_nro)
);

CREATE TABLE camilomartinez."SoporteCine"(
	cine_id text,
	cine_nombre text,
	cine_ubicacion text,
	PRIMARY KEY (cine_id)
);

CREATE TABLE camilomartinez."CiudadCine"(
	cine_id text,
	ciudad_nombre text,
	PRIMARY KEY (cine_id, ciudad_nombre)
);

CREATE TABLE camilomartinez."CineSala"(
	sala_nro int,
	cine_id text,
	PRIMARY KEY ( sala_nro, cine_id)
);

CREATE TABLE camilomartinez."PeliculaFuncion" (
	funcion_fecha_hora timestamp,
	porcentaje_ocupacion text,
	pelicula_nombre text,
	PRIMARY KEY (funcion_fecha_hora, pelicula_nombre)
);

CREATE TABLE camilomartinez."SoporteTarjeta" (
	tarjeta_nro bigint,
	tarjeta_fecha text,
	tarjeta_banco text,
	PRIMARY KEY (tarjeta_nro)
);

CREATE TABLE camilomartinez."SoporteTipoBoleto"(
	tipo_boleto text,
	descuento int,
	PRIMARY KEY (tipo_boleto)
);

CREATE TABLE camilomartinez."UsuarioReservacion"(
	usuario_dni text,
	usuario_nombre text,
	reservacion_nro text,
	PRIMARY KEY ( (usuario_dni, reservacion_nro), usuario_nombre)
) WITH CLUSTERING ORDER BY ( usuario_nombre ASC);


CREATE TABLE camilomartinez."ReservacionTipoBoleto"(
	reservacion_nro text,
	tipo_boleto_nombre text,
	nro_boletos int,
	PRIMARY KEY ( (reservacion_nro, tipo_boleto_nombre), nro_boletos)
) WITH CLUSTERING ORDER BY ( nro_boletos ASC);


CREATE TABLE camilomartinez."SoporteReservacion" (
	reservacion_nro text,
	reservacion_confirmado boolean,
	funcion_fecha_hora date,
	pelicula_nombre text,
	PRIMARY KEY (reservacion_nro, pelicula_nombre, funcion_fecha_hora)
);
