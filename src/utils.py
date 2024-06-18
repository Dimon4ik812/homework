import csv
import json
import re
from collections import Counter
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
            xlsx_transactions = []
            for index, row in df.iterrows():
                transactions = {
                    'id': row['id'],
                    'state': row['state'],
                    'date': row['date'],
                    'operationAmount': {
                        'amount': row['amount'],
                        'currency': {
                            'name': row['currency_name'],
                            'code': row['currency_name']
                        }
                    },
                    'description': row['description'],
                    'from': row['from'],
                    'to': row['to']
                }
                xlsx_transactions.append(transactions)
            return xlsx_transactions
        else:
            logger.error("Неподреживаемый формат файла *")
            return []
    except (FileNotFoundError, json.JSONDecodeError, pd.errors.EmptyDataError) as e:
        logger.error(f"Произошла ошибка {e}")
        return []


def search_transactions(transactions: list, search_string: str) -> dict:
    """функция которая фильтруем список словарей по заданной строке поиска"""
    filtered_transactions = []
    for transaction in transactions:
        if re.search(search_string, transaction['description'], re.IGNORECASE):
            filtered_transactions.append(transaction)
    return filtered_transactions



def get_counter_categories(transactions: list, list_categories: list) -> dict:
    """Функция которая подсчитывает количество операций в категории"""
    operations_categories = []
    for transaction in transactions:
        for category in list_categories:
            if category in transaction['description']:
                operations_categories.append(category)
    return dict(Counter(operations_categories))

