import pytest

from src.widget import mask_account_card

@pytest.mark.parametrize("account_card, expected",
                         [('7000792289606361', '7000 79** **** 6361'),
                          ('Счет 64686473678894779589', 'Счет **9589')])
def test_widget(account_card, expected):
    assert mask_account_card(account_card) == expected
