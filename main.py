import os
from typing import Any

from src.decorators import log
from src.external_api import convert_to_rub
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import account_disguise, masking_card_number
from src.processing import filtering_words_by_key, sort_descending
from src.utils import get_transactions, search_transactions, get_counter_categories
from src.widget import date_decoding, data_masking_function

# input_data = [
#     {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
# ]
#
#
# transactions = [
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702",
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188",
#     },
#     {
#         "id": 873106923,
#         "state": "EXECUTED",
#         "date": "2019-03-23T01:09:46.296404",
#         "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 44812258784861134719",
#         "to": "Счет 74489636417521191160",
#     },
#     {
#         "id": 895315941,
#         "state": "EXECUTED",
#         "date": "2018-08-19T04:27:37.904916",
#         "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод с карты на карту",
#         "from": "Visa Classic 6831982476737658",
#         "to": "Visa Platinum 8990922113665229",
#     },
#     {
#         "id": 594226727,
#         "state": "CANCELED",
#         "date": "2018-09-12T21:27:25.241689",
#         "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод организации",
#         "from": "Visa Platinum 1246377376343588",
#         "to": "Счет 14211924144426031657",
#     },
# ]

# output_data = date_decoding("2018-07-11T02:26:18.671407")
# print(output_data)
#
# mask_card_number = masking_card_number("7000792289606361")
# print(mask_card_number)
#
# mask_account = account_disguise("73654108430135874305")
# print(mask_account)
#
# check_first_func = filtering_words_by_key(input_data)
#
# for i in check_first_func:
#     print(i)
#
#
# check_second_func = sort_descending(input_data)
# for i in check_second_func:
#     print(i)
#
#
# usd_transactions = filter_by_currency(transactions, "USD")
#
# for _ in range(3):
#     print(next(usd_transactions)["id"])
#
#
# descriptions = transaction_descriptions(transactions)
#
# for _ in range(5):
#     print(next(descriptions))
#
#
# for card_number in card_number_generator(1, 5):
#     print(card_number)
#
#
# @log(filename="mylog.txt")
# def my_function(x: int, y: int) -> int:
#     """функция вызова декоратора с запись в'mylog.txt'"""
#     return x + y
#
#
# my_function(1, 2)
#
#
# @log(filename="mylog.txt")
# def my_function_error(x: int, y: Any) -> None:
#     """функция вызова декоратора с ошибок и записью в 'mylog.txt'"""
#     return x + y
#
#
# my_function_error(1, "2")
#
#
# @log()
# def my_function_not_file(x: int, y: int) -> int:
#     """функция вызова декоратора с выводом результата в консоль"""
#     return x + y
#
#
# my_function_not_file(1, 2)
#
#
# @log()
# def my_function_not_file_error(x: int, y: Any) -> None:
#     """функция вызова декоратора с ошибкой и выводом в консоль"""
#     return x + y
#
#
# my_function_not_file_error(1, "2")
#
#
# # Путь до файла с данными о финансовых транзакциях
# current_dir = os.path.dirname(os.path.abspath(__file__))
# json_file_path = os.path.join(current_dir, "data", "operations.json")
# transactions = get_transactions(json_file_path)
# print(transactions)
#
#
# for transaction in transactions:
#     rub_amount = convert_to_rub(transaction)
#
#     print(f"Transaction amount in RUB: {rub_amount}")
# current_dir = os.path.dirname(os.path.abspath(__file__))
# csv_file_path = os.path.join(current_dir, "data", "transactions.csv")
# transactions = get_transactions(csv_file_path)
# list_categories = ['Перевод с карты на карту', 'Открытие вклада']
# counter_categories = get_counter_categories(transactions, list_categories)
# print(counter_categories)
# filter_transactions = search_transactions(transactions, "Перевод организации")
# for transaction in filter_transactions:
#     print(transaction)
# file_path = '../data/perations.json'
#
while True:
    print('''Привет! Добро пожаловать в программу работы
        с банковскими транзакциями.
        Выберите необходимый пункт меню:
            1. Получить информацию о транзакциях из JSON-файла
            2. Получить информацию о транзакциях из CSV-файла
            3. Получить информацию о транзакциях из XLSX-файла''')
    user_input = input('Выберите формат файла 1/2/3:')
    if user_input == '1':
        json_file_path = 'data/operations.json'
        transactions = get_transactions(json_file_path)
        break
    elif user_input == '2':
        csv_file_path = 'data/transactions.csv'
        transactions = get_transactions(csv_file_path)
        break
    elif user_input == '3':
        excel_file_path = 'data/transactions_excel.xlsx'
        transactions = get_transactions(excel_file_path)
        break
    else:
        print('НЕ ПРАВИЛЬНЫЙ ФОРМАТ ВВОДА!!! ВВЕДИТЕ 1, 2 или 3')
        continue
while True:
    print('''Введите статус, по которому необходимо выполнить
фильтрацию.''')
    user_input = input('Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING:').upper()
    if user_input in ['EXECUTED', 'CANCELED', 'PENDING']:
        filter_operations = filtering_words_by_key(transactions, user_input)
        print(f'операции отфильтрованны по статусу: {user_input}')
        break
    else:
        print(f'статус операции {user_input} не доступен')
while True:
    print('Отсортировать операции по дате?')
    input_date_sorting = input('Да/Нет:').lower()
    if input_date_sorting == 'нет':
        counter_categories = get_counter_categories(filter_operations, ['Перевод со счета на счет','Перевод организации', 'Перевод с карты на карту', 'Открытие вклада'])
        count = 0
        for values in counter_categories.values():
            count += values
        print(f' Всего банковских операций в выборке: {count}')
        for operations in filter_operations:
            if operations['description'].lower() == 'открытие вклада':
                print(f'{date_decoding(operations['date'])} {operations['description']}\n'
                      f' {data_masking_function(operations['to'])}')
            else:
                print(f'{date_decoding(operations['date'])} {operations['description']}\n'
                      f'{data_masking_function(operations['from'])} -> {data_masking_function(operations['to'])}')
            break
    elif input_date_sorting not in ['да', 'нет']:
        print(f'{input_date_sorting} не верный ввод')
        continue
    elif input_date_sorting == 'да':
        print('Отсортировать по возрастанию или по убыванию? ')
        input_sorting_direction = input('по возрастанию/по убыванию:').lower()
        if input_sorting_direction == 'по возрастанию':
            data_sort = sort_descending(filter_operations, False)
        elif input_sorting_direction == 'по убыванию':
            data_sort = sort_descending(filter_operations, True)
        else:
            print(f'{input_sorting_direction} не верное направление сортировки')
            continue

        print('Выводить только рублевые тразакции?')
        input_currency = input('Да/Нет:').lower()
        if input_currency == 'да':
            filter_currency = filter_by_currency(data_sort, 'RUB')
        elif input_currency == 'нет':
            filter_currency = data_sort
        else:
            print(f'{input_currency} не верный ввод')

        print('Отфильтровать список транзакций по определенному слову в описании? ')
        input_filter_by_word = input('Да/Нет:').lower()
        if input_filter_by_word == 'нет':
            result = filter_currency
            for operations in filter_currency:
                if operations['description'].lower() == 'открытие вклада':
                    print(f'{date_decoding(operations['date'])} {operations['description']}\n'
                          f' {data_masking_function(operations['to'])}\n'
                          f'{operations['operationAmount']['amount']}')
                else:
                    print(f'{date_decoding(operations['date'])} {operations['description']}\n'
                          f'{data_masking_function(operations['from'])} -> {data_masking_function(operations['to'])}\n'
                          f'{operations['operationAmount']['amount']}')
                    break
        elif input_filter_by_word == 'да':
            word_input = input('Введите слова по которому отфильровать список:')
            result = search_transactions(filter_currency)
        else:
            print(f'{input_filter_by_word} не верный ввод')



