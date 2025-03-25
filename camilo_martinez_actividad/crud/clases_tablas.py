import datetime

from dataclasses import dataclass

import datetime
from dataclasses import dataclass

# Tabla 1: Pacientes Info (Pacientes por su nombre)
@dataclass
class Tabla1:
    paciente_nombre: str
    paciente_dni: str
    paciente_fecha_nac: datetime.date
    paciente_direccion: str
    paciente_tlf: str
    paciente_alergias: set

    def __str__(self):
        return f'Nombre: {self.paciente_nombre}, DNI: {self.paciente_dni}, Fecha Nac: {self.paciente_fecha_nac}, Dir: {self.paciente_direccion}, Tlf: {self.paciente_tlf}, Alergias: {self.paciente_alergias}'

    def __dict__(self):
        return {
            'paciente_nombre': self.paciente_nombre,
            'paciente_dni': self.paciente_dni,
            'paciente_fecha_nac': self.paciente_fecha_nac,
            'paciente_direccion': self.paciente_direccion,
            'paciente_tlf': self.paciente_tlf,
            'paciente_alergias': self.paciente_alergias
        }

# Tabla 2: Citas por Medico (Citas atendidas por un medico)
@dataclass
class Tabla2:
    medico_dni: str
    cita_id: str
    cita_fecha_hora: datetime.datetime
    cita_motivo: str

    def __str__(self):
        return f'Medico DNI: {self.medico_dni}, Cita ID: {self.cita_id}, Fecha Hora: {self.cita_fecha_hora}, Motivo: {self.cita_motivo}'

    def __dict__(self):
        return {
            'medico_dni': self.medico_dni,
            'cita_id': self.cita_id,
            'cita_fecha_hora': self.cita_fecha_hora,
            'cita_motivo': self.cita_motivo
        }

# Tabla 3: Tratamientos por paciente (Tratamientos incluidos en las citas de un paciente)
@dataclass
class Tabla3:
    paciente_dni: str
    cita_id: str
    tratamiento_id: str
    tratamiento_descripcion: str
    tratamiento_costo: float

    def __str__(self):
        return f'Paciente DNI: {self.paciente_dni}, Cita ID: {self.cita_id}, Tratamiento ID: {self.tratamiento_id}, Descripcion: {self.tratamiento_descripcion}, Costo: {self.tratamiento_costo}'

    def __dict__(self):
        return {
            'paciente_dni': self.paciente_dni,
            'cita_id': self.cita_id,
            'tratamiento_id': self.tratamiento_id,
            'tratamiento_descripcion': self.tratamiento_descripcion,
            'tratamiento_costo': self.tratamiento_costo
        }

# Tabla 4: Citas por paciente (Conteo de citas por paciente)
@dataclass
class Tabla4:
    paciente_dni: str
    cita_id: int # counter en Cassandra se representa como int en Python

    def __str__(self):
        return f'Paciente DNI: {self.paciente_dni}, Cita ID: {self.cita_id}'

    def __dict__(self):
        return {
            'paciente_dni': self.paciente_dni,
            'cita_id': self.cita_id
        }

# Tabla 5: Recetas x Medicamentos (Relación n-m - Medicamentos incluidos en una receta)
@dataclass
class Tabla5:
    receta_fecha_emision: datetime.date
    receta_id: str
    medicamento_codigo: str
    medicamento_nombre: str
    medicamento_dosis: str

    def __str__(self):
        return f'Fecha Emision: {self.receta_fecha_emision}, Receta ID: {self.receta_id}, Medicamento Codigo: {self.medicamento_codigo}, Nombre: {self.medicamento_nombre}, Dosis: {self.medicamento_dosis}'

    def __dict__(self):
        return {
            'receta_fecha_emision': self.receta_fecha_emision,
            'receta_id': self.receta_id,
            'medicamento_codigo': self.medicamento_codigo,
            'medicamento_nombre': self.medicamento_nombre,
            'medicamento_dosis': self.medicamento_dosis
        }

# Tabla 6: Pacientes por alergia (Pacientes con una alergia especifica)
@dataclass
class Tabla6:
    paciente_alergia: str
    paciente_nombre: str
    paciente_dni: str
    paciente_fecha_nac: datetime.date
    paciente_direccion: str
    paciente_tlf: str

    def __str__(self):
        return f'Alergia: {self.paciente_alergia}, Nombre: {self.paciente_nombre}, DNI: {self.paciente_dni}, Fecha Nac: {self.paciente_fecha_nac}, Dir: {self.paciente_direccion}, Tlf: {self.paciente_tlf}'

    def __dict__(self):
        return {
            'paciente_alergia': self.paciente_alergia,
            'paciente_nombre': self.paciente_nombre,
            'paciente_dni': self.paciente_dni,
            'paciente_fecha_nac': self.paciente_fecha_nac,
            'paciente_direccion': self.paciente_direccion,
            'paciente_tlf': self.paciente_tlf
        }

# Tabla 7: SoportePaciente (Entidad Paciente)
@dataclass
class SoportePaciente:
    paciente_dni: str
    paciente_nombre: str
    paciente_fecha_nac: datetime.date
    paciente_direccion: str
    paciente_tlf: str
    paciente_alergias: set

    def __str__(self):
        return f'DNI: {self.paciente_dni}, Nombre: {self.paciente_nombre}, Fecha Nac: {self.paciente_fecha_nac}, Dir: {self.paciente_direccion}, Tlf: {self.paciente_tlf}, Alergias: {self.paciente_alergias}'

    def __dict__(self):
        return {
            'paciente_dni': self.paciente_dni,
            'paciente_nombre': self.paciente_nombre,
            'paciente_fecha_nac': self.paciente_fecha_nac,
            'paciente_direccion': self.paciente_direccion,
            'paciente_tlf': self.paciente_tlf,
            'paciente_alergias': self.paciente_alergias
        }

# Tabla 8: SoporteMedico (Entidad Medico)
@dataclass
class SoporteMedico:
    medico_dni: str
    medico_nombre: str
    medico_fecha_nac: datetime.date
    medico_tlf: str
    medico_especialidades: set

    def __str__(self):
        return f'DNI: {self.medico_dni}, Nombre: {self.medico_nombre}, Fecha Nac: {self.medico_fecha_nac}, Tlf: {self.medico_tlf}, Especialidades: {self.medico_especialidades}'

    def __dict__(self):
        return {
            'medico_dni': self.medico_dni,
            'medico_nombre': self.medico_nombre,
            'medico_fecha_nac': self.medico_fecha_nac,
            'medico_tlf': self.medico_tlf,
            'medico_especialidades': self.medico_especialidades
        }

# Tabla 9: SoporteCita (Entidad Cita)
@dataclass
class SoporteCita:
    cita_id: str
    cita_fecha_hora: datetime.datetime
    cita_motivo: str
    paciente_dni: str
    medico_dni: str

    def __str__(self):
        return f'ID: {self.cita_id}, Fecha Hora: {self.cita_fecha_hora}, Motivo: {self.cita_motivo}, Paciente DNI: {self.paciente_dni}, Medico DNI: {self.medico_dni}'