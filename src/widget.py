from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_type: str) -> str:
    """
    Функция принимает счет или карту с номером и возвращает замаскированный номер карты или счета
    """
    number = 0
    for char in number_type:
        if not char.isdigit():
            number += 1
    if "Счет" in number_type or "счет" in number_type:
        number_mask = get_mask_account(number_type)
        return number_mask
    else:
        number_mask = get_mask_card_number(number_type[number:])
        return "".join({number_type[:number]+number_mask})
