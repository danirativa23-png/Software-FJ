
import unittest

from clases.cliente import Cliente
from clases.reserva_sala import ReservaSala
from clases.alquiler_equipo import AlquilerEquipo
from clases.asesoria import Asesoria
from clases.reserva import Reserva
from utilidades.excepciones import (
    ClienteNoEncontradoError,
    ReservaNoValidaError,
    EstadoReservaError
)


class PruebasSistema(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente(
            "C001",
            "Daniel Ramirez",
            "12345678",
            "daniel@gmail.com",
            "3001234567"
        )

        self.sala = ReservaSala(
            "S001", "Sala principal", "Sala para reuniones",
            100000, 20, ["Proyector", "Internet"]
        )

        self.equipo = AlquilerEquipo(
            "E001", "Computadores", "Alquiler de computadores",
            50000, 2, "Portátil"
        )

        self.asesoria = Asesoria(
            "A001", "Asesoría técnica", "Orientación especializada",
            80000, "Tecnología", 2
        )

    def test_cliente_valido(self):
        self.assertEqual(self.cliente.nombre, "Daniel Ramirez")

    def test_cliente_documento_invalido(self):
        with self.assertRaises(ValueError):
            Cliente("C002", "Carlos Perez", "ABC", "carlos@gmail.com", "3001234567")

    def test_cliente_correo_invalido(self):
        with self.assertRaises(ValueError):
            Cliente("C003", "Carlos Perez", "12345678", "correo_invalido", "3001234567")

    def test_cliente_telefono_invalido(self):
        with self.assertRaises(ValueError):
            Cliente("C004", "Carlos Perez", "12345678", "carlos@gmail.com", "123")

    def test_reserva_sala(self):
        self.assertEqual(self.sala.capacidad, 20)

    def test_alquiler_equipo(self):
        self.assertEqual(self.equipo.cantidad, 2)

    def test_asesoria(self):
        self.assertEqual(self.asesoria.especialidad, "Tecnología")

    def test_calculo_costo_sala(self):
        self.assertAlmostEqual(self.sala.calcular_costo(), 100000)

    def test_calculo_costo_equipo(self):
        self.assertAlmostEqual(self.equipo.calcular_costo(), 100000)

    def test_calculo_costo_asesoria(self):
        self.assertAlmostEqual(self.asesoria.calcular_costo(), 160000)

    def test_crear_reserva(self):
        reserva = Reserva("R001", self.cliente, self.sala, 2)
        self.assertEqual(reserva.estado, "Pendiente")

    def test_reserva_sin_cliente(self):
        with self.assertRaises(ClienteNoEncontradoError):
            Reserva("R002", None, self.sala, 1)

    def test_reserva_duracion_invalida(self):
        with self.assertRaises(ReservaNoValidaError):
            Reserva("R003", self.cliente, self.sala, 0)

    def test_confirmar_reserva(self):
        reserva = Reserva("R004", self.cliente, self.sala, 1)
        reserva.confirmar()
        self.assertEqual(reserva.estado, "Confirmada")

    def test_cancelar_reserva(self):
        reserva = Reserva("R005", self.cliente, self.sala, 1)
        reserva.cancelar()
        self.assertEqual(reserva.estado, "Cancelada")

    def test_procesar_reserva(self):
        reserva = Reserva("R006", self.cliente, self.sala, 1)
        reserva.confirmar()
        reserva.procesar()
        self.assertEqual(reserva.estado, "Procesada")

    def test_confirmar_reserva_cancelada(self):
        reserva = Reserva("R007", self.cliente, self.sala, 1)
        reserva.cancelar()

        with self.assertRaises(EstadoReservaError):
            reserva.confirmar()


if __name__ == "__main__":
    unittest.main(verbosity=2)
