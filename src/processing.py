def filtering_words_by_key(word_list: list, state: str = "EXECUTED") -> list:
    """Функция фильтрует список словарей по ключу state"""
    new_list = []
    for word in word_list:
        if word.get("state") == state:
            new_list.append(word)
    return new_list


def sort_descending(word_list: list, direction: bool = True) -> list:
    """Функция сортирует словари по дате"""
    sorted_list = sorted(word_list, key=lambda x: x["date"], reverse=direction)
    return sorted_list
