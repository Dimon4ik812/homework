import logging
import os
from typing import Any


def setup_logging(name: str, log_file: str) -> Any:
    """функция для создания логгера"""
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(log_file, mode="w")
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger
