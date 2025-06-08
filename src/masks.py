def get_mask_card_number(card_numder: str) -> str:
    """
    Принимает на вход номер карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """

    masked_number = card_numder[:4] + " " + card_numder[4:6] + "**" + " **** " + card_numder[-4:]

    return masked_number


print(get_mask_card_number("7000792289606361"))


def get_mask_account(score_number: str) -> str:
    """
    Принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X — это цифра номера.
    То есть видны только последние 4 цифры номера, а перед ними — две звездочки.
    """
    masked_score = "**" + score_number[-4:]
    return masked_score


print(get_mask_account("73654108430135874305"))
