# === Stage 6: Фильтрация записей ===
# Project: PotteryLog
from datetime import date


def filter_by_clay_type(items, clay_type):
    return [item for item in items if item.get("clay_type") == clay_type]


def filter_by_date_range(items, start_date, end_date):
    return [
        item
        for item in items
        if start_date <= item.get("date") <= end_date
    ]


def filter_items(items, clay_type=None, start_date=None, end_date=None):
    result = items
    if clay_type is not None:
        result = filter_by_clay_type(result, clay_type)
    if start_date is not None and end_date is not None:
        result = filter_by_date_range(result, start_date, end_date)
    return result


if __name__ == "__main__":
    sample_items = [
        {"id": 1, "name": "Чашка", "clay_type": "керамика", "weight": 320, "date": date(2024, 1, 15), "status": "готово"},
        {"id": 2, "name": "Ваза", "clay_type": "глина", "weight": 1200, "date": date(2024, 2, 20), "status": "готово"},
        {"id": 3, "name": "Миска", "clay_type": "керамика", "weight": 450, "date": date(2024, 3, 10), "status": "готово"},
        {"id": 4, "name": "Тарелка", "clay_type": "глина", "weight": 280, "date": date(2024, 4, 5), "status": "готово"},
        {"id": 5, "name": "Кувшин", "clay_type": "керамика", "weight": 700, "date": date(2024, 5, 1), "status": "готово"},
    ]

    print("Все изделия:", len(sample_items))
    print("Изделия из керамики:", len(filter_by_clay_type(sample_items, "керамика")))
    print("Изделия за январь-март:", len(filter_by_date_range(sample_items, date(2024, 1, 1), date(2024, 3, 31))))
    print("Керамика за январь-март:", len(filter_items(sample_items, "керамика", date(2024, 1, 1), date(2024, 3, 31))))
