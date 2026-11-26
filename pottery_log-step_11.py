# === Stage 11: Постраничный вывод ===
# Project: PotteryLog
from typing import List, Dict, Any


class Pagination:
    def __init__(self, page: int, page_size: int):
        if page < 1:
            page = 1
        if page_size < 1:
            page_size = 1
        self.page = page
        self.page_size = page_size

    def get_page_size(self) -> int:
        return self.page_size

    def get_page(self) -> int:
        return self.page

    def has_next(self) -> bool:
        return self.page * self.page_size < len(self.items)

    def has_prev(self) -> bool:
        return self.page > 1

    def total_pages(self, total_items: int) -> int:
        return (total_items + self.page_size - 1) // self.page_size

    def get_next_page(self) -> int:
        return self.page + 1

    def get_prev_page(self) -> int:
        return self.page - 1

    def get_page_items(self, items: List[Any]) -> List[Any]:
        start = (self.page - 1) * self.page_size
        end = start + self.page_size
        return items[start:end]

    def set_page(self, page: int) -> None:
        self.page = page if page >= 1 else 1

    def set_page_size(self, page_size: int) -> None:
        self.page_size = page_size if page_size >= 1 else 1

    def to_dict(self) -> Dict[str, Any]:
        return {
            "page": self.page,
            "page_size": self.page_size,
            "total_pages": self.total_pages(len(self.items)),
            "has_next": self.has_next(),
            "has_prev": self.has_prev(),
        }


def build_pagination(page: int, page_size: int, items: List[Any]) -> Pagination:
    if items is None:
        items = []
    return Pagination(page, page_size)


def paginate_items(items: List[Any], page: int, page_size: int) -> Dict[str, Any]:
    p = Pagination(page, page_size)
    p.items = items
    return {
        "items": p.get_page_items(items),
        "page": p.page,
        "page_size": p.page_size,
        "total_pages": p.total_pages(len(items)),
        "has_next": p.has_next(),
        "has_prev": p.has_prev(),
    }


def get_page_items(items: List[Any], page: int, page_size: int) -> List[Any]:
    p = Pagination(page, page_size)
    return p.get_page_items(items)
