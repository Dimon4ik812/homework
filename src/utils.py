import json
import os


def get_transactions(file_path: str) -> list[dict]:
    """
    Функция, которая принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            repos = json.load(file)
            if isinstance(repos, list):
                return repos
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# file_path = '../data/operations.json'
# transaction = load_transactions(file_path)

# Путь до файла с данными о финансовых транзакциях
current_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(current_dir, "../data", "operations.json")
transactions = get_transactions(json_file_path)
print(transactions)
