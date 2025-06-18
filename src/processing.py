from typing import List, Dict, Union, Any
from datetime import datetime

list_of_operations: List[Dict[str, Union[str, int]]] = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


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


print(sort_by_date(list_of_operations))


def filter_by_state(list_of_operations: List[Dict[str, Any]], state: str = "EXECUTED") -> list[Dict[str, Any]]:
    """ "
    Функция выдает только список словарей, у которых параметр "state" = "EXECUTED"
    """
    return list((item for item in list_of_operations if item.get("state") == state))


print(filter_by_state(list_of_operations))
