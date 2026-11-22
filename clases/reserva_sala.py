
from clases.servicio import Servicio


class ReservaSala(Servicio):
    """Servicio de reserva de salas para reuniones y eventos."""

    def __init__(self, identificador, nombre, descripcion, tarifa_base,
                 capacidad, recursos):
        super().__init__(identificador, nombre, descripcion, tarifa_base)
        self.validar_parametros(capacidad=capacidad, recursos=recursos)
        self.capacidad = capacidad
        self.recursos = recursos

    def validar_parametros(self, **kwargs):
        capacidad = kwargs.get("capacidad")
        recursos = kwargs.get("recursos")

        if not isinstance(capacidad, int) or isinstance(capacidad, bool) or capacidad <= 0:
            raise ValueError("La capacidad debe ser un número entero mayor que cero.")

        if not isinstance(recursos, list) or not recursos:
            raise ValueError("Debe registrar al menos un recurso para la sala.")

    def calcular_costo(self, impuesto=0, descuento=0):
        if impuesto < 0 or descuento < 0 or descuento > 100:
            raise ValueError("Impuesto o descuento no válido.")

        subtotal = self.tarifa_base
        total = subtotal * (1 - descuento / 100)
        return total * (1 + impuesto / 100)

    def describir(self):
        return (
            f"Sala {self.nombre}: capacidad para {self.capacidad} personas. "
            f"Recursos: {', '.join(self.recursos)}."
        )

    def mostrar_informacion(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Tarifa: ${self.tarifa_base:,.2f} | "
            f"{self.describir()}"
        )
