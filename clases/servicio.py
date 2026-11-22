
from abc import abstractmethod
from clases.entidad import Entidad


class Servicio(Entidad):
    """Clase abstracta para los servicios de Software FJ."""

    def __init__(self, identificador, nombre, descripcion, tarifa_base):
        super().__init__(identificador)

        self.nombre = nombre
        self.descripcion = descripcion
        self.tarifa_base = tarifa_base

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del servicio no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La descripción no puede estar vacía.")
        self._descripcion = valor.strip()

    @property
    def tarifa_base(self):
        return self._tarifa_base

    @tarifa_base.setter
    def tarifa_base(self, valor):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool) or valor <= 0:
            raise ValueError("La tarifa debe ser un número mayor que cero.")
        self._tarifa_base = float(valor)

    @abstractmethod
    def mostrar_informacion(self):
        pass

    @abstractmethod
    def calcular_costo(self, impuesto=0, descuento=0):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self, **kwargs):
        pass
