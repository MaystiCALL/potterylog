# === Stage 7: Сортировка записей ===
# Project: PotteryLog
from __future__ import annotations

from datetime import datetime

__all__ = ["sort_by_name", "sort_by_created_at", "sort_records"]


def sort_by_name(records, reverse: bool = False) -> list:
    return sorted(records, key=lambda r: r["name"], reverse=reverse)


def sort_by_created_at(records, reverse: bool = False) -> list:
    return sorted(
        records,
        key=lambda r: r.get("created_at") or datetime.min,
        reverse=reverse,
    )


def sort_records(
    records,
    field: str = "name",
    reverse: bool = False,
) -> list:
    if field == "created_at":
        return sort_by_created_at(records, reverse=reverse)
    return sort_by_name(records, reverse=reverse)
