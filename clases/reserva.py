
from datetime import datetime
from utilidades.excepciones import (
    ClienteNoEncontradoError,
    ReservaNoValidaError,
    ServicioNoDisponibleError,
    EstadoReservaError
)
from utilidades.logger_config import logger


class Reserva:
    """Gestiona las reservas de clientes y servicios."""

    def __init__(self, identificador, cliente, servicio, duracion):
        if cliente is None:
            raise ClienteNoEncontradoError("La reserva necesita un cliente válido.")

        if servicio is None:
            raise ServicioNoDisponibleError("La reserva necesita un servicio válido.")

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ReservaNoValidaError("La duración debe ser mayor que cero.")

        self._identificador = identificador
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = "Pendiente"
        self._fecha_creacion = datetime.now()

        logger.info("Reserva %s creada para el cliente %s.",
                    identificador, cliente.nombre)

    @property
    def identificador(self):
        return self._identificador

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    def confirmar(self):
        if self._estado != "Pendiente":
            raise EstadoReservaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        self._estado = "Confirmada"
        logger.info("Reserva %s confirmada.", self._identificador)

    def cancelar(self):
        if self._estado not in ("Pendiente", "Confirmada"):
            raise EstadoReservaError(
                "No se puede cancelar esta reserva."
            )

        self._estado = "Cancelada"
        logger.info("Reserva %s cancelada.", self._identificador)

    def procesar(self):
        if self._estado != "Confirmada":
            raise EstadoReservaError(
                "La reserva debe estar confirmada para procesarse."
            )

        self._estado = "Procesada"
        logger.info("Reserva %s procesada.", self._identificador)

    def calcular_total(self, impuesto=0, descuento=0):
        try:
            costo = self._servicio.calcular_costo(impuesto, descuento)
            return costo * self._duracion
        except (ValueError, TypeError) as error:
            logger.exception("Error al calcular el costo de la reserva.")
            raise ReservaNoValidaError(
                "No fue posible calcular el costo de la reserva."
            ) from error

    def mostrar_informacion(self):
        return (
            f"Reserva: {self._identificador}\n"
            f"Cliente: {self._cliente.nombre}\n"
            f"Servicio: {self._servicio.nombre}\n"
            f"Duración: {self._duracion}\n"
            f"Estado: {self._estado}\n"
            f"Fecha: {self._fecha_creacion.strftime('%d/%m/%Y %H:%M')}"
        )
