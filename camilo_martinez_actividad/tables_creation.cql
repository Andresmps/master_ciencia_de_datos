--create keyspace camilomartinez with durable_writes = true and replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

use camilomartinez

--- drop table camilomartinez."Tabla1";
--- drop table camilomartinez."Tabla2";
--- drop table camilomartinez."Tabla3";
--- drop table camilomartinez."Tabla4";
--- drop table camilomartinez."Tabla5";
--- drop table camilomartinez."Tabla6";
--- drop table camilomartinez."soportepaciente";
--- drop table camilomartinez."soportemedico";


-- Tabla 1: Pacientes Info (Pacientes por su nombre)
CREATE TABLE camilomartinez."Tabla1"(
    paciente_nombre text,
    paciente_dni int,
    paciente_fecha_nac date,
    paciente_direccion text,
    paciente_tlf text,
    paciente_alergias SET<text>,
    PRIMARY KEY (paciente_nombre, paciente_dni)
) WITH CLUSTERING ORDER BY (paciente_dni asc);

-- Tabla 2: Citas por Medico (Citas atendidas por un medico)
CREATE TABLE camilomartinez."Tabla2"(
    medico_dni int,
    cita_id int,
    cita_fecha_hora timestamp,
    cita_motivo text,
    PRIMARY KEY (medico_dni, cita_id)
) WITH CLUSTERING ORDER BY (cita_id ASC);

-- Tabla 3: Tratamientos por paciente (Tratamientos incluidos en las citas de un paciente)
CREATE TABLE camilomartinez."Tabla3"(
    paciente_dni int,
    cita_id int,
    tratamiento_id int,
    tratamiento_descripcion text,
    tratamiento_costo float,
    PRIMARY KEY (paciente_dni, cita_id, tratamiento_id)
) WITH CLUSTERING ORDER BY (cita_id asc, tratamiento_id asc);

-- Tabla 4: Citas por paciente (Conteo de citas por paciente)
CREATE TABLE camilomartinez."Tabla4"(
    paciente_dni int,
    cita_id counter,
    PRIMARY KEY (paciente_dni)
);

-- Tabla 5: Recetas x Medicamentos (Relación n-m - Medicamentos incluidos en una receta)
CREATE TABLE camilomartinez."Tabla5"(
    receta_fecha_emision date,
    receta_id int,
    medicamento_codigo int,
    medicamento_nombre text,
    medicamento_dosis text,
    PRIMARY KEY (receta_fecha_emision, receta_id, medicamento_codigo)
) WITH CLUSTERING ORDER BY (receta_id ASC, medicamento_codigo ASC);

-- Tabla 6: Pacientes por alergia (Pacientes con una alergia especifica)
CREATE TABLE camilomartinez."Tabla6"(
    paciente_alergia text,
    paciente_nombre text,
    paciente_dni int,
    paciente_fecha_nac date,
    paciente_direccion text,
    paciente_tlf text,
    PRIMARY KEY (paciente_alergia, paciente_dni)
) WITH CLUSTERING ORDER BY (paciente_dni ASC);

-- SoportePaciente Table
CREATE TABLE SoportePaciente (
    paciente_dni int PRIMARY KEY,
    paciente_nombre text,
    paciente_fecha_nac date,
    paciente_direccion text,
    paciente_tlf text,
    paciente_alergias set<text>
);

-- SoporteMedico Table
CREATE TABLE SoporteMedico (
    medico_dni int PRIMARY KEY,
    medico_nombre text,
    medico_fecha_nac date,
    medico_tlf text,
    medico_especialidades set<text>
);

-- SoporteCita Table
CREATE TABLE SoporteCita (
    cita_id text PRIMARY KEY,
    cita_fecha_hora timestamp,
    cita_motivo text,
    paciente_dni int, -- Foreign Key to SoportePaciente
    medico_dni int -- Foreign Key to SoporteMedico
);

-- SoporteReceta Table
CREATE TABLE SoporteReceta (
    receta_id int PRIMARY KEY,
    receta_fecha_emision timestamp,
    medico_dni int -- Foreign Key to SoporteMedico
);

-- SoporteTratamiento Table
CREATE TABLE SoporteTratamiento (
    tratamiento_id int PRIMARY KEY,
    tratamiento_descripcion text,
    tratamiento_costo decimal,
    tratamiento_numero int,
    tratamiento_hospital text,
    tratamiento_ciudad text
);

-- SoporteMedicamento Table
CREATE TABLE SoporteMedicamento (
    medicamento_codigo int PRIMARY KEY,
    medicamento_nombre text,
    medicamento_dosis text
);

-- SoporteCitaTratamiento (Relationship between Cita and Tratamiento)
CREATE TABLE SoporteCitaTratamiento (
    cita_id int, -- Foreign Key to SoporteCita
    tratamiento_id int, -- Foreign Key to SoporteTratamiento
    PRIMARY KEY (cita_id, tratamiento_id)
);

-- SoporteRecetaMedicamento (Relationship between Receta and Medicamento)
CREATE TABLE SoporteRecetaMedicamento (
    receta_id int, -- Foreign Key to SoporteReceta
    medicamento_codigo int, -- Foreign Key to SoporteMedicamento
    PRIMARY KEY (receta_id, medicamento_codigo)
);