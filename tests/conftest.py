import pytest

import sys

import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def card():
    return '7000 79** **** 6361'


@pytest.fixture
def score():
    return 'Счет **9589'
