import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def masking_card_number(number: str) -> str:
    """функция принимает номер карты и возвращает его зашифрованным"""
    string_number = str(number)
    filter_number = ""
    masking_number = ""
    logger.info("Маскируем номер карты символом *")
    for i, digit in enumerate(string_number):
        if 6 <= i < 12:
            masking_number += "*"
        else:
            masking_number += digit
    logger.info("добавляем пробел после каждой 4ой цифры")
    for i, digit in enumerate(masking_number, start=1):
        filter_number += digit
        if i % 4 == 0:
            filter_number += " "
    return filter_number


def account_disguise(number: str) -> str:
    """Функция принимает номер счета и возвращает его маску"""
    logger.info("Маскируем номер счета в формате ** и 4 последнии цифры")
    string_number = str(number)
    masked_number = "**" + string_number[-4:]
    return masked_number


# mask_card_number = masking_card_number('7000792289606361')
# print(mask_card_number)
#
# mask_account = account_disguise('73654108430135874305')
# print(mask_account)
