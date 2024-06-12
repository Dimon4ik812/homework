import csv
import json

import pandas as pd

from src.logger import setup_logging

logger = setup_logging("utils", "logs/utils.log")


def get_transactions(file_path: str) -> list[dict]:
    """
    Функция, которая принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        if file_path.endswith(".json"):
            logger.info("открываем json файл *")
            with open(file_path, "r", encoding="utf-8") as file:
                repos = json.load(file)
                logger.info("Проверка содержимого в файле")
                if isinstance(repos, list):
                    return repos
                else:
                    return []
        elif file_path.endswith(".csv"):
            logger.info("открываем csv файл *")
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file, delimiter=";")
                return list(reader)
        elif file_path.endswith(".xlsx"):
            logger.info("открываем excel файл *")
            df = pd.read_excel(file_path)
            return df.to_dict(orient="records")
        else:
            logger.error("Неподреживаемый формат файла *")
            return []
    except (FileNotFoundError, json.JSONDecodeError, pd.errors.EmptyDataError) as e:
        logger.error(f"Произошла ошибка {e}")
        return []
