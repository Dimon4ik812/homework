from typing import Any

from src.generators import get_transactions_filter_by_rub
from src.processing import filtering_words_by_key, sort_descending
from src.utils import get_transactions, search_transactions
from src.widget import data_masking_function, date_decoding


def main() -> Any:
    while True:
        print(
            """Привет! Добро пожаловать в программу работы
            с банковскими транзакциями.
            Выберите необходимый пункт меню:
                1. Получить информацию о транзакциях из JSON-файла
                2. Получить информацию о транзакциях из CSV-файла
                3. Получить информацию о транзакциях из XLSX-файла"""
        )
        user_input = input("Выберите формат файла 1/2/3:")
        if user_input == "1":
            json_file_path = "data/operations.json"
            transactions = get_transactions(json_file_path)
            break
        elif user_input == "2":
            csv_file_path = "data/transactions.csv"
            transactions = get_transactions(csv_file_path)
            break
        elif user_input == "3":
            excel_file_path = "data/transactions_excel.xlsx"
            transactions = get_transactions(excel_file_path)
            break
        else:
            print("НЕ ПРАВИЛЬНЫЙ ФОРМАТ ВВОДА!!! ВВЕДИТЕ 1, 2 или 3")
            continue
    while True:
        print(
            """Введите статус, по которому необходимо выполнить
    фильтрацию."""
        )
        user_input = input("Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING:").upper()
        if user_input in ["EXECUTED", "CANCELED", "PENDING"]:
            filter_operations = filtering_words_by_key(transactions, user_input)
            print(f"операции отфильтрованны по статусу: {user_input}")
            break
        else:
            print(f"статус операции {user_input} не доступен")
            continue
    while True:
        print("Отсортировать операции по дате?")
        input_date_sorting = input("Да/Нет:").lower()
        if input_date_sorting == "нет":
            data_sort = filter_operations
            break
        elif input_date_sorting not in ["да", "нет"]:
            print(f"{input_date_sorting} не верный ввод")
            continue
        elif input_date_sorting == "да":
            print("Отсортировать по возрастанию или по убыванию? ")
            input_sorting_direction = input("по возрастанию/по убыванию:").lower()
            if input_sorting_direction == "по возрастанию":
                data_sort = sort_descending(filter_operations, False)
                break
            elif input_sorting_direction == "по убыванию":
                data_sort = sort_descending(filter_operations, True)
                break
            else:
                print(f"{input_sorting_direction} не верное направление сортировки")
                continue
    while True:
        print("Выводить только рублевые тразакции?")
        input_currency = input("Да/Нет:").lower()
        if input_currency == "да":
            filter_currency = get_transactions_filter_by_rub(data_sort, "RUB")
            break
        elif input_currency == "нет":
            filter_currency = data_sort
            break
        else:
            print(f"{input_currency} не верный ввод")
            continue
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? ")
        input_filter_by_word = input("Да/Нет:").lower()
        if input_filter_by_word == "нет":
            result = filter_currency
            print("Распечатываю итоговый список транзакций...")
            print(f"Всего банковских операций в выборке: {len(result)}")
            for operations in result:
                if operations["description"].lower() == "открытие вклада":
                    print(
                        f"{date_decoding(operations['date'])} {operations['description']}\n"
                        f" {data_masking_function(operations['to'])}\n"
                        f"{operations['operationAmount']['amount']} "
                        f"{operations['operationAmount']['currency']['name']}"
                    )
                else:
                    print(
                        f"{date_decoding(operations['date'])} {operations['description']}\n"
                        f"{data_masking_function(operations['from'])} -> {data_masking_function(operations['to'])}\n"
                        f"{operations['operationAmount']['amount']} "
                        f"{operations['operationAmount']['currency']['name']}"
                    )
            break
        elif input_filter_by_word == "да":
            search_key = input("Введите слова для фильтрации:")
            result = search_transactions(filter_currency, search_key)
            print("Распечатываю итоговый список транзакций...")
            print(f" Всего банковских операций в выборке: {len(result)}")
            for operations in result:
                if operations["description"].lower() == "открытие вклада":
                    print(
                        f"{date_decoding(operations['date'])} {operations['description']}\n"
                        f" {data_masking_function(operations['to'])}\n"
                        f"{operations['operationAmount']['amount']} "
                        f"{operations['operationAmount']['currency']['name']}"
                    )
                else:
                    print(
                        f"{date_decoding(operations['date'])} {operations['description']}\n"
                        f"{data_masking_function(operations['from'])} -> "
                        f"{data_masking_function(operations['to'])}\n"
                        f"{operations['operationAmount']['amount']} "
                        f"{operations['operationAmount']['currency']['name']}"
                    )
            break
        else:
            print(f"{input_filter_by_word} не правильный ввод")


if __name__ == "__main__":
    main()
