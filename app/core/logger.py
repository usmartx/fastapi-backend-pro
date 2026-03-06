import logging

# Création du logger
logger = logging.getLogger("backend_pro")
logger.setLevel(logging.INFO)

# Format des messages
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# StreamHandler pour console
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)