
from clases.servicio import Servicio


class AlquilerEquipo(Servicio):
    """Servicio de alquiler de equipos tecnológicos."""

    def __init__(self, identificador, nombre, descripcion, tarifa_base,
                 cantidad, tipo_equipo):
        super().__init__(identificador, nombre, descripcion, tarifa_base)
        self.validar_parametros(cantidad=cantidad, tipo_equipo=tipo_equipo)
        self.cantidad = cantidad
        self.tipo_equipo = tipo_equipo

    def validar_parametros(self, **kwargs):
        cantidad = kwargs.get("cantidad")
        tipo_equipo = kwargs.get("tipo_equipo")

        if not isinstance(cantidad, int) or isinstance(cantidad, bool) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero mayor que cero.")

        if not isinstance(tipo_equipo, str) or not tipo_equipo.strip():
            raise ValueError("Debe indicar el tipo de equipo.")

    def calcular_costo(self, impuesto=0, descuento=0):
        if impuesto < 0 or descuento < 0 or descuento > 100:
            raise ValueError("Impuesto o descuento no válido.")

        subtotal = self.tarifa_base * self.cantidad
        total = subtotal * (1 - descuento / 100)
        return total * (1 + impuesto / 100)

    def describir(self):
        return (
            f"Alquiler de {self.cantidad} unidad(es) de "
            f"{self.tipo_equipo}."
        )

    def mostrar_informacion(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Tarifa por unidad: ${self.tarifa_base:,.2f} | "
            f"{self.describir()}"
        )
