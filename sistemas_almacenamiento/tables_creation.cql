create keyspace camilomartinez with durable_writes = true and replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

use camilomartinez

CREATE TABLE camilomartinez."Tabla1"(
	pelicula_categoria text,
	pelicula_nombre text,
	pelicula_actores SET<text>,
	PRIMARY KEY (pelicula_categoria, pelicula_nombre)
) WITH CLUSTERING ORDER BY ( pelicula_nombre asc );

CREATE TABLE camilomartinez."Tabla2"(
	usuario_dni text,
	reservacion_nro text,
	tipo_boleto_nombre text,cre
	PRIMARY KEY (usuario_dni, reservacion_nro, tipo_boleto_nombre)
) WITH CLUSTERING ORDER BY ( reservacion_nro ASC, tipo_boleto_nombre ASC );

CREATE TABLE camilomartinez."Tabla3"(
	cine_nombre text,
	sala_nro int,
	PRIMARY KEY (cine_nombre, sala_nro)
) WITH CLUSTERING ORDER BY ( sala_nro ASC )

CREATE TABLE camilomartinez."Tabla4"(
	usuario_dni text,
	reservacion_nro counter,
	PRIMARY KEY (usuario_dni)
)

CREATE TABLE camilomartinez."Tabla5"(
	tarjeta_banco text,
	tarjeta_nro int,
	reservacion_nro int,
	reservacion_confirmado boolean,
	PRIMARY KEY (tarjeta_banco, tarjeta_nro, reservacion_nro)
) WITH CLUSTERING ORDER BY ( tarjeta_nro ASC, reservacion_nro ASC );

CREATE TABLE camilomartinez."Tabla6"(
	pelicula_categoria text,
	pelicula_nombre text,
	pelicula_actores set<text>,
	PRIMARY KEY ((pelicula_categoria), pelicula_nombre)
) WITH CLUSTERING ORDER BY ( pelicula_nombre ASC )

CREATE TABLE camilomartinez."Tabla7"(
	usuario_tlf text,
	usuario_dni text,
	usuario_nombre text,
	usuario_tlfs set<text>,
	PRIMARY KEY (usuario_tlf, usuario_dni)
) WITH CLUSTERING ORDER BY ( usuario_dni ASC );

CREATE TABLE camilomartinez."Tabla8"(
	ciudad_nombre text,
	pelicula_nombre text,
	funcion_fecha_hora date,
	PRIMARY KEY ( ciudad_nombre, pelicula_nombre, funcion_fecha_hora)
) WITH CLUSTERING ORDER BY ( pelicula_nombre ASC, funcion_fecha_hora ASC );

CREATE TABLE camilomartinez."SoporteCine"(
	cine_id text,
  	cine_nombre text,
	cine_ubicacion text,
	PRIMARY KEY (cine_id)
);

CREATE TABLE camilomartinez."SoportePelicula"(
	pelicula_nombre text,
  	pelicula_categoria text,
	pelicula_actores set<text>,
	PRIMARY KEY (pelicula_nombre)
);

CREATE TABLE camilomartinez."SoporteUsuario" (
	usuario_dni text,
	usuario_nombre text,
	usuario_tlfs SET<text>,
	PRIMARY KEY (usuario_dni)
);

CREATE TABLE camilomartinez."SoporteReservacion" (
	reservacion_nro int,
	reservacion_confirmado boolean,
	PRIMARY KEY (reservacion_nro)
);

CREATE TABLE camilomartinez."SoporteTarjeta" (
	tarjeta_nro int,
	tarjeta_fecha text,
	tarjeta_banco text,
	PRIMARY KEY (tarjeta_nro)
);
