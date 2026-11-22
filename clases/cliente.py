
from clases.entidad import Entidad


class Cliente(Entidad):
    """Representa un cliente del sistema Software FJ."""

    def __init__(self, identificador, nombre, documento, correo, telefono):
        super().__init__(identificador)

        self.nombre = nombre
        self.documento = documento
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres.")
        self._nombre = valor.strip()

    @property
    def documento(self):
        return self._documento

    @documento.setter
    def documento(self, valor):
        valor = str(valor).strip()
        if not valor.isdigit() or len(valor) < 5:
            raise ValueError("El documento debe contener al menos 5 números.")
        self._documento = valor

    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        if not isinstance(valor, str) or "@" not in valor or "." not in valor.split("@")[-1]:
            raise ValueError("El correo electrónico no es válido.")
        self._correo = valor.strip().lower()

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        valor = str(valor).strip()
        if not valor.isdigit() or len(valor) < 7:
            raise ValueError("El teléfono debe contener al menos 7 números.")
        self._telefono = valor

    def mostrar_informacion(self):
        return (
            f"Cliente: {self.nombre} | "
            f"Documento: {self.documento} | "
            f"Correo: {self.correo} | "
            f"Teléfono: {self.telefono}"
        )
