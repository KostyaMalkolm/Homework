from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card):
    assert get_mask_card_number('7000792289606361') == card


def test_get_mask_account(score):
    assert get_mask_account('Счет 64686473678894779589') == score
