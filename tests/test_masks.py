import pytest

from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'

def test_get_mask_account():
    assert get_mask_account('Счет 64686473678894779589') == 'Счет **9589'