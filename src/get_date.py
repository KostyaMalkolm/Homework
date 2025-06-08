from datetime import datetime


def get_date(iso_date: str) -> str:

    """
    Форматирование даты и времени под формат ДД.ММ.ГГГГ
    """

    return datetime.fromisoformat(iso_date).strftime('%d.%m.%Y')


print(get_date("2024-03-11T02:26:18.671407"))
