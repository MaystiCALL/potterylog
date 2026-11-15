# === Stage 5: Генерация идентификаторов ===
# Project: PotteryLog
import uuid
from typing import Iterable


def generate_project_id(prefix: str, existing: Iterable[str]) -> str:
    """Генерирует уникальный идентификатор с префиксом проекта.

    Префикс берётся из параметра и дополняется случайным значением длиной
    8 символов из безопасного алфавита. Если сгенерированная строка уже
    присутствует в списке уже занятых идентификаторов, генерация повторяется,
    пока не получится уникальное значение.

    Args:
        prefix: строка-префикс, уникальная для проекта.
        existing: итерируемый объект с уже существующими идентификаторами.

    Returns:
        строка с уникальным идентификатором проекта.

    Raises:
        ValueError: если список занятых идентификаторов слишком велик для
            генерации уникального значения в разумное число попыток.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    max_attempts = 1000

    occupied = set(existing)
    for _ in range(max_attempts):
        candidate = prefix + "".join(
            alphabet[int(uuid.uuid4().hex[i * 2: i * 2 + 2], 16) if i < 4 else 0]
            for i in range(8)
        )
        if candidate not in occupied:
            return candidate

    raise ValueError(
        f"Не удалось сгенерировать уникальный идентификатор: "
        f"слишком много занятых значений ({len(occupied)})."
    )


def build_unique_ids(items: Iterable[dict], prefix: str) -> dict:
    """Присваивает уникальные идентификаторы изделиям гончарной мастерской.

    Идентификаторы генерируются с префиксом проекта и проверяются на
    коллизии. Возвращается словарь, связывающий исходный объект изделия с
    присвоенным идентификатором.

    Args:
        items: итерируемый объект изделий мастерской.
        prefix: строка-префикс для идентификаторов.

    Returns:
        словарь вида {изделие: идентификатор}.
    """
    return {item: generate_project_id(prefix, assigned.values()) for item, assigned in zip(items, _iter_assign(items))}


def _iter_assign(items: Iterable[dict]) -> Iterable[dict]:
    """Помогает генерировать идентификаторы по одному для каждого изделия."""
    for item in items:
        yield {
            "id": generate_project_id(prefix, assigned.values()),
        }
