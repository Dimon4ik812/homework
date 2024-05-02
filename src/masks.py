def masking_card_number(number: int) -> str:
    """функция принимает номер карты и возвращает его зашифрованным"""
    string_number = str(number)
    filter_number = ""
    masking_number = ""
    for i, digit in enumerate(string_number):
        if 6 <= i < 12:
            masking_number += "*"
        else:
            masking_number += digit

    for i, digit in enumerate(masking_number, start=1):
        filter_number += digit
        if i % 4 == 0:
            filter_number += " "
    return filter_number


def account_disguise(number: int) -> str:
    """Функция принимает номер счета и возвращает его маску"""
    string_number = str(number)
    masked_number = "**" + string_number[-4:]
    return masked_number
