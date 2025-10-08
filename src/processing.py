from typing import List, Dict, Union, Any
from datetime import datetime


def filter_by_state(list_of_operations: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict]:
    """ "
    Функция выдает только список словарей, у которых параметр "state" = "EXECUTED"
    """
    return list((item for item in list_of_operations if item.get("state") == state))


def sort_by_date(sorting: List[Dict[str, Union[str, int]]], reverse: bool = True) -> List[Dict[str, Union[str, int]]]:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате.
    """
    operation_of_sorting = sorting.copy()
    operation_of_sorting.sort(
        key=lambda x: datetime.fromisoformat(x["date"]) if isinstance(x["date"], str) else datetime.min,
        reverse=reverse,
    )

    return operation_of_sorting
