from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_type: str) -> str:
    """
    Функция принимает счет или карту с номером и возвращает замаскированный номер карты или счета
    """
    length_name_card_or_score = 0
    for char in number_type:
        if not char.isdigit():
            length_name_card_or_score += 1
    if "Счет" in number_type or "счет" in number_type:
        number_mask = get_mask_account(number_type[length_name_card_or_score:])
        return "".join(number_type[0:length_name_card_or_score] + number_mask)
    else:
        number_mask = get_mask_card_number(number_type[length_name_card_or_score:])
        return "".join({number_type[0:length_name_card_or_score]+number_mask})


number_type = input()


print(mask_account_card(number_type))
