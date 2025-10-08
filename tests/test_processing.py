from typing import Dict

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(filter_operations: list[Dict], filter_result_operations: list[Dict]) -> None:
    assert filter_by_state(filter_operations) == filter_result_operations


def test_sort_by_date(filter_operations: list[Dict], sort_result_date: list[Dict]) -> None:
    assert sort_by_date(filter_operations) == sort_result_date
