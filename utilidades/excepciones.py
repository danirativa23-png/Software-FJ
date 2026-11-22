
class ErrorSistema(Exception):
    """Excepción base para los errores de Software FJ."""
    pass


class ClienteNoEncontradoError(ErrorSistema):
    """Se genera cuando no se encuentra un cliente."""
    pass


class ReservaNoValidaError(ErrorSistema):
    """Se genera cuando una reserva no cumple las condiciones."""
    pass


class ServicioNoDisponibleError(ErrorSistema):
    """Se genera cuando un servicio no está disponible."""
    pass


class EstadoReservaError(ErrorSistema):
    """Se genera cuando una operación no es válida para el estado de la reserva."""
    pass
