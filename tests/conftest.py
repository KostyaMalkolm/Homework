import pytest


@pytest.fixture
def card() -> str:
    return '7000 79** **** 6361'


@pytest.fixture
def score() -> str:
    return 'Счет **9589'

@pytest.fixture
def date() -> str:
    return '11.03.2024'

@pytest.fixture
def operations() -> str:
    return '[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]'

@pytest.fixture
def sort_date() -> str:
    return ''