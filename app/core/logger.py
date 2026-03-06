# app/core/logger.py
import logging

# Création d’un logger pour toute l’application
logger = logging.getLogger("backend_pro_logger")
logger.setLevel(logging.INFO)

# Format des logs
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Handler console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)