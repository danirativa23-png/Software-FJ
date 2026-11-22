
from clases.servicio import Servicio


class Asesoria(Servicio):
    """Servicio de asesorías especializadas."""

    def __init__(self, identificador, nombre, descripcion, tarifa_base,
                 especialidad, duracion_horas):
        super().__init__(identificador, nombre, descripcion, tarifa_base)
        self.validar_parametros(
            especialidad=especialidad,
            duracion_horas=duracion_horas
        )
        self.especialidad = especialidad
        self.duracion_horas = duracion_horas

    def validar_parametros(self, **kwargs):
        especialidad = kwargs.get("especialidad")
        duracion = kwargs.get("duracion_horas")

        if not isinstance(especialidad, str) or not especialidad.strip():
            raise ValueError("Debe indicar la especialidad de la asesoría.")

        if not isinstance(duracion, (int, float)) or isinstance(duracion, bool) or duracion <= 0:
            raise ValueError("La duración debe ser mayor que cero.")

    def calcular_costo(self, impuesto=0, descuento=0):
        if impuesto < 0 or descuento < 0 or descuento > 100:
            raise ValueError("Impuesto o descuento no válido.")

        subtotal = self.tarifa_base * self.duracion_horas
        total = subtotal * (1 - descuento / 100)
        return total * (1 + impuesto / 100)

    def describir(self):
        return (
            f"Asesoría en {self.especialidad} "
            f"con duración de {self.duracion_horas} hora(s)."
        )

    def mostrar_informacion(self):
        return (
            f"Servicio: {self.nombre} | "
            f"Tarifa por hora: ${self.tarifa_base:,.2f} | "
            f"{self.describir()}"
        )
