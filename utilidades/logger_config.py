
import logging
import os


def configurar_logger():
    """Configura el registro de eventos y errores del sistema."""

    carpeta_logs = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "logs"
    )

    os.makedirs(carpeta_logs, exist_ok=True)

    ruta_log = os.path.join(carpeta_logs, "software_fj.log")

    logger = logging.getLogger("SoftwareFJ")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        manejador = logging.FileHandler(ruta_log, encoding="utf-8")
        formato = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        manejador.setFormatter(formato)
        logger.addHandler(manejador)

    return logger


logger = configurar_logger()
