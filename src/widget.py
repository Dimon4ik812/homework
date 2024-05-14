from src.masks import account_disguise, masking_card_number


def data_masking_function(user_data: str) -> str:
    """функция принимает тип карты/счета и номер/карты счета и маскирует их"""
    if 'Счет'.lower() in user_data.lower():
        result = account_disguise(user_data)
        return result
    else:
        card_type = ''
        card_number = ''
        for i in user_data:
            if i.isdigit():
                card_number += i
            else:
                card_type += i

        filter_card_number = masking_card_number(int(card_number))
        return card_type + filter_card_number



def date_decoding(encrypted_date: str) -> str:
    """функция принимает дату и переворачивает ее"""
    data_parts = encrypted_date.split('T')[0].split('-')
    return '.'.join(data_parts[::-1])

