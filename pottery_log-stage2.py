# === Stage 2: Проверка полей ===
# Project: PotteryLog
"""Модуль валидации и нормализации полей сущности «изделие» для PotteryLog."""

import re

MIN_WEIGHT = 0.0
MAX_WEIGHT = 100000.0
ALLOWED_STATUSES = ("готово", "обжигается", "сырое", "брошено", "на реставрации")
GLAZE_PATTERNS = (
    r"глазурь",
    r"глина",
    r"керамика",
    r"фарфор",
    r"порцелан",
    r"каolin",
    r"каолин",
)


def normalize_input(value):
    """Приводит строку к виду, удобному для хранения в журнале.

    - обрезает лишние пробелы по краям,
    - сводит внутренние пробелы к одиночным,
    - убирает управляющие символы,
    - приводит к нижнему регистру,
    - обнуляет пробелы внутри слов.
    """
    if value is None:
        return ""
    if not isinstance(value, str):
        value = str(value)
    value = value.strip().replace("\t", " ").replace("\r", " ").replace("\n", " ")
    value = re.sub(r"[^\S \n]", " ", value)
    value = re.sub(r"\s+", " ", value).strip()
    value = value.lower()
    value = re.sub(r"\s+", " ", value).strip()
    return value


def clean_glaze_type(glaze_type):
    """Нормализует тип глины: убирает лишние пробелы и переводит в нижний регистр."""
    if glaze_type is None:
        return ""
    cleaned = normalize_input(glaze_type)
    for pattern in GLAZE_PATTERNS:
        if re.search(pattern, cleaned):
            return cleaned
    return cleaned


def validate_name(name):
    """Проверяет поле «название» изделия."""
    if name is None or name.strip() == "":
        raise ValueError("Название изделия не может быть пустым.")
    cleaned = normalize_input(name)
    if len(cleaned) < 2:
        raise ValueError("Название должно содержать минимум два символа.")
    if len(cleaned) > 100:
        raise ValueError("Название не может превышать 100 символов.")
    if not re.search(r"[a-zа-яё]", cleaned):
        raise ValueError("Название должно содержать букву.")
    return cleaned


def validate_clay_type(clay_type):
    """Проверяет поле «тип глины» изделия."""
    if clay_type is None or clay_type.strip() == "":
        raise ValueError("Тип глины не может быть пустым.")
    cleaned = clean_glaze_type(clay_type)
    if len(cleaned) < 2:
        raise ValueError("Тип глины должен содержать минимум два символа.")
    if len(cleaned) > 100:
        raise ValueError("Тип глины не может превышать 100 символов.")
    if not re.search(r"[a-zа-яё]", cleaned):
        raise ValueError("Тип глины должен содержать букву.")
    return cleaned


def validate_weight(weight):
    """Проверяет числовое поле «вес» изделия."""
    try:
        value = float(weight)
    except (TypeError, ValueError):
        raise ValueError("Вес должен быть числом.")
    if value != value:
        raise ValueError("Вес не может быть некорректным значением.")
    if value <= 0:
        raise ValueError("Вес должен быть положительным числом.")
    if value > MAX_WEIGHT:
        raise ValueError(f"Вес не может превышать {MAX_WEIGHT:g} граммов.")
    return round(value, 3)


def validate_status(status):
    """Проверяет поле «статус» изделия."""
    if status is None or status.strip() == "":
        raise ValueError("Статус не может быть пустым.")
    normalized = normalize_input(status)
    if normalized not in ALLOWED_STATUSES:
        raise ValueError(
            f"Статус должен быть одним из: {', '.join(ALLOWED_STATUSES)}."
        )
    return normalized


def validate_item(name, clay_type, weight, status):
    """Валидирует все поля сущности «изделие» и возвращает нормализованные значения."""
    return (
        validate_name(name),
        validate_clay_type(clay_type),
        validate_weight(weight),
        validate_status(status),
    )
