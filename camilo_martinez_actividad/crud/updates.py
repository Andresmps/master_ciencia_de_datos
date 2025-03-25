import logging

from dataclasses import dataclass

from .utils import TipoOperacion, queryStringTemplates, Logging

from .selects import Selects
from .inserts import Inserts
from .deletes import Deletes

logging.basicConfig(
    format=Logging.MSG_FORMAT.value,
    datefmt=Logging.DATETIME_FORMAT.value, level=logging.INFO,
)

logger = logging.getLogger(Logging.UPDATES_LOGGER.value)

@dataclass
class Updates:
    session: object

    def actualizarDireccionPaciente(
            self, paciente_dni: int = None, paciente_direccion: str = None):
        """
            Descripción: Función para actualizar la dirección de un paciente
        """
        _select_instance = Selects(self.session)
        _insert_instance = Inserts(self.session)
        _delete_instance = Deletes(self.session)

        paciente_dni = \
            int(input('Ingrese el DNI del paciente: ')) if paciente_dni is None else paciente_dni

        paciente_nueva_direccion = \
            input('Ingrese la nueva dirección del paciente: ')\
            if paciente_direccion is None else paciente_direccion

        _paciente = _select_instance.selectDatosPaciente(usuario_dni=paciente_dni)

        if _paciente is None:
            logger.error(f'El paciente con DNI {paciente_dni} no existe.')
            return

        _direccion = _paciente.paciente_direccion
        _nombre = _paciente.paciente_nombre
        _fecha_nac = _paciente.paciente_fecha_nac
        _tlf = _paciente.paciente_tlf
        _alergias = _paciente.paciente_alergias

        _insert_instance.insertar_tabla1(
            paciente_nombre=_nombre, paciente_dni=paciente_dni, paciente_fecha_nac=_fecha_nac,
            paciente_direccion=paciente_nueva_direccion, paciente_tlf=_tlf, paciente_alergias=_alergias
        )

        _delete_instance.eliminar_registro_tabla1(
            paciente_direccion=_direccion, paciente_nombre=_nombre
        )

        self.actualizarSoportePaciente(
            paciente_dni=paciente_dni, paciente_nueva_direccion=paciente_nueva_direccion
        )

    def actualizarSoportePaciente(
            self, paciente_dni: int = None, paciente_nueva_direccion: str = None):
        """
            Descripción: Función para actualizar la dirección de un paciente
        """
        _query_update_soporte_paciente = queryStringTemplates(
            tabla='soportepaciente', columnas=[], tipo_operacion=TipoOperacion.UPDATE.value,
            where_columns=['paciente_dni'], update_column='paciente_direccion',
            update_value=paciente_nueva_direccion
        )

        logger.info(f'Actualizando la dirección del paciente con DNI {paciente_dni} en la tabla SoportePaciente.')
        logger.info(f'Query: {_query_update_soporte_paciente}')
        _update_statement = self.session.prepare(_query_update_soporte_paciente)
        self.session.execute(_update_statement, [paciente_dni])
        logger.info(f'Actualización de la dirección del paciente con DNI {paciente_dni} exitosa.')
