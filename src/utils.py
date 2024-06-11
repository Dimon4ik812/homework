import json
import logging
import pandas as pd
import csv

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions(file_path: str) -> list[dict]:
    """
    Функция, которая принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        if file_path.endswith('.json'):
            logger.info(f"открываем json файл *")
            with open(file_path, "r", encoding="utf-8") as file:
                repos = json.load(file)
                logger.info("Проверка содержимого в файле")
                if isinstance(repos, list):
                    return repos
                else:
                    return []
        elif file_path.endswith('.csv'):
            logger.info(f'открываем csv файл *')
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return list(reader)
        elif file_path.endswith('.xlsx'):
            logger.info(f"открываем excel файл *")
            df = pd.read_excel(file_path)
            return df.to_dict(orient='records')
        else:
            logger.error(f'Неподреживаемый формат файла: {file_path}')
            return []
    except (FileNotFoundError, json.JSONDecodeError, pd.errors.EmptyDataError) as e:
        logger.error(f"Произошла ошибка {e}")
        return []


# df = pd.read_excel('transactions_excel')
#
# with open('../data/transactions.csv') as st_file:
#     reader = csv.reader(st_file)
#     # next(reader)
#     for row in reader:
#         print(row)

