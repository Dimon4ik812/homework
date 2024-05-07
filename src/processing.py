from typing import List

def function_of_filtering_words_by_key(word_list: list,
                                       state='EXECUTED') -> list:
    """Функция фильтрует список словарей по ключу state"""
    new_list = []
    for word in word_list:
        if word.get('state') == state:
            new_list.append(word)
    return new_list






