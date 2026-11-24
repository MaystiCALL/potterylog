# === Stage 10: Группировка ===
# Project: PotteryLog
from collections import Counter


def clay_type_counts(pots):
    """Группирует изделия по полю 'тип глины' и считает количество в каждой группе.

    Возвращает словарь вида {'Красная глина': 3, 'Белая глина': 2}.
    """
    types = [pot['тип глины'] for pot in pots]
    return dict(Counter(types))
