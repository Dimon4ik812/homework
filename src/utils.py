import json
import os

def load_transaction(file_path):
    """загружаем данные о финансовых транзакциях из JSON-файла"""
    try:
        if not os.path.exists(file_path):
            return []

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if not isinstance(data, list):
            return []

        return data
    except (json.JSONDecodeError, IOError):
        return []


if __name__ == '__main__':
    file_path = '../data/operations.json'
    transactions = load_transaction(file_path)
    for transaction in transactions:
        print(transaction)