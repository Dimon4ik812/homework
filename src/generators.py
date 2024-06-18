import re
from typing import Generator, List


def filter_by_currency(transactions: List[dict], currency: str) -> Generator:
    """Функция принимает список словарей и фильтрует его по валюте"""
    transaction1 = []
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            transaction1.append(transaction)
            yield transaction1


def transaction_descriptions(transactions: List[dict]) -> Generator:
    """Функция возвращает описание каждой операции по очереди"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Функция генерирует номер банковской карты"""
    for num in range(start, end + 1):
        card_number = "{:016d}".format(num)
        formatted_card_number = " ".join([card_number[i : i + 4] for i in range(0, len(card_number), 4)])
        yield formatted_card_number


def get_transactions_filter_by_rub(transactions: list, search_key: str) -> list:
    """Функция фильтрации транзакций по коду валюты"""
    result = []
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and re.search(search_key, transaction["operationAmount"]["currency"]["code"], re.IGNORECASE)
        ):
            result.append(transaction)
    return result
