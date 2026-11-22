
from clases.cliente import Cliente
from clases.reserva_sala import ReservaSala
from clases.alquiler_equipo import AlquilerEquipo
from clases.asesoria import Asesoria
from clases.reserva import Reserva
from utilidades.logger_config import logger
from utilidades.excepciones import ErrorSistema

# Listas principales del sistema
clientes = []
servicios = []
reservas = []


# Cargar los servicios disponibles
def cargar_servicios():
    servicios.clear()

    servicios.extend([
        ReservaSala(
            "S001",
            "Sala principal",
            "Sala para reuniones",
            100000,
            20,
            ["Proyector", "Internet"]
        ),
        AlquilerEquipo(
            "E001",
            "Computadores",
            "Alquiler de equipos",
            50000,
            2,
            "Portátil"
        ),
        Asesoria(
            "A001",
            "Asesoría técnica",
            "Orientación especializada",
            80000,
            "Tecnología",
            2
        )
    ])


# Registrar un cliente
def registrar_cliente():
    try:
        print("\n--- REGISTRAR CLIENTE ---")

        cliente = Cliente(
            input("Identificador: ").strip(),
            input("Nombre: ").strip(),
            input("Documento: ").strip(),
            input("Correo: ").strip(),
            input("Teléfono: ").strip()
        )

        if any(c.documento == cliente.documento for c in clientes):
            print("Ese documento ya está registrado.")
            return

        clientes.append(cliente)
        logger.info("Cliente registrado: %s", cliente.nombre)

        print("Cliente registrado correctamente.")

    except ValueError as error:
        print("Error al registrar el cliente:", error)
        logger.error("Error al registrar cliente: %s", error)

    except Exception as error:
        print("Se presentó un error inesperado:", error)
        logger.exception("Error inesperado al registrar cliente")


# Mostrar clientes registrados
def mostrar_clientes():
    print("\n--- CLIENTES REGISTRADOS ---")

    if len(clientes) == 0:
        print("No hay clientes registrados.")
        return

    for numero, cliente in enumerate(clientes, start=1):
        print(f"\nCliente {numero}")
        print(cliente.mostrar_informacion())


# Mostrar servicios disponibles
def mostrar_servicios():
    print("\n--- SERVICIOS DISPONIBLES ---")

    if len(servicios) == 0:
        print("No hay servicios disponibles.")
        return

    for numero, servicio in enumerate(servicios, start=1):
        print(f"\n{numero}. {servicio.mostrar_informacion()}")


# Crear una reserva
def crear_reserva():
    try:
        print("\n--- CREAR RESERVA ---")

        if not clientes:
            print("Primero debe registrar un cliente.")
            return

        mostrar_clientes()

        documento = input("\nDocumento del cliente: ").strip()

        cliente = next(
            (c for c in clientes if c.documento == documento),
            None
        )

        if cliente is None:
            print("Cliente no encontrado.")
            return

        mostrar_servicios()

        opcion = input("\nSeleccione el servicio (1, 2 o 3): ").strip()

        if not opcion.isdigit():
            print("Debe ingresar un número.")
            return

        numero_servicio = int(opcion)

        if numero_servicio < 1 or numero_servicio > len(servicios):
            print("El servicio seleccionado no existe.")
            return

        duracion = float(input("Ingrese la duración: "))

        reserva = Reserva(
            f"R{len(reservas) + 1:03d}",
            cliente,
            servicios[numero_servicio - 1],
            duracion
        )

        reservas.append(reserva)

        print("\nReserva creada correctamente.")
        print(reserva.mostrar_informacion())

    except (ValueError, ErrorSistema) as error:
        print("No fue posible crear la reserva:", error)
        logger.error("Error al crear reserva: %s", error)

    except Exception as error:
        print("Ocurrió un error inesperado:", error)
        logger.exception("Error inesperado al crear reserva")


# Gestionar una reserva
def gestionar_reserva():
    try:
        print("\n--- GESTIONAR RESERVA ---")

        if not reservas:
            print("No hay reservas registradas.")
            return

        mostrar_reservas()

        codigo = input("\nCódigo de la reserva: ").strip()

        reserva = next(
            (r for r in reservas if r.identificador == codigo),
            None
        )

        if reserva is None:
            print("Reserva no encontrada.")
            return

        print("\n1. Confirmar reserva")
        print("2. Cancelar reserva")
        print("3. Procesar reserva")

        opcion = input("Seleccione una operación: ").strip()

        if opcion == "1":
            reserva.confirmar()
            print("Reserva confirmada correctamente.")

        elif opcion == "2":
            reserva.cancelar()
            print("Reserva cancelada correctamente.")

        elif opcion == "3":
            reserva.procesar()
            print("Reserva procesada correctamente.")

        else:
            print("Opción no válida.")

    except ErrorSistema as error:
        print("No fue posible gestionar la reserva:", error)
        logger.error("Error al gestionar reserva: %s", error)

    except Exception as error:
        print("Ocurrió un error inesperado:", error)
        logger.exception("Error inesperado al gestionar reserva")


# Mostrar todas las reservas
def mostrar_reservas():
    print("\n--- RESERVAS REGISTRADAS ---")

    if len(reservas) == 0:
        print("No hay reservas registradas.")
        return

    for reserva in reservas:
        print(reserva.mostrar_informacion())
        print("-" * 40)


# Menú principal
def menu():
    cargar_servicios()

    while True:
        print("\n====================================")
        print("       SISTEMA INTEGRAL SOFTWARE FJ")
        print("====================================")
        print("1. Registrar cliente")
        print("2. Mostrar clientes")
        print("3. Mostrar servicios")
        print("4. Crear reserva")
        print("5. Gestionar reserva")
        print("6. Mostrar reservas")
        print("7. Salir")
        print("====================================")

        opcion = input("Seleccione una opción: ").strip()
        print("OPCION RECIBIDA:", repr(opcion))

        if opcion == "1":
            registrar_cliente()

        elif opcion == "2":
            mostrar_clientes()

        elif opcion == "3":
            mostrar_servicios()

        elif opcion == "4":
            crear_reserva()

        elif opcion == "5":
            gestionar_reserva()

        elif opcion == "6":
            mostrar_reservas()

        elif opcion == "7":
            print("\nGracias por utilizar Software FJ.")
            logger.info("Sistema cerrado correctamente.")
            break

        else:
            print("\nOpción no válida. Intente nuevamente.")


# Ejecutar el programa
if __name__ == "__main__":
    try:
        menu()

    except KeyboardInterrupt:
        print("\nEl sistema fue interrumpido por el usuario.")
        logger.warning("Ejecución interrumpida.")

    except Exception as error:
        print("\nError general del sistema:", error)
        logger.exception("Error general de ejecución.")

    finally:
        print("\nAplicación finalizada.")
