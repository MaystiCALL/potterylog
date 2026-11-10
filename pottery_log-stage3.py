# === Stage 3: Хранилище в памяти ===
# Project: PotteryLog
import threading
from collections import OrderedDict


class PotteryItem:
    """Изделие гончарной мастерской.

    Поля: название, тип глины, вес, статус.
    """

    def __init__(self, name, clay_type, weight, status="в работе"):
        self.name = name
        self.clay_type = clay_type
        self.weight = weight
        self.status = status

    def __repr__(self):
        return f"PotteryItem(name={self.name!r}, clay_type={self.clay_type!r}, weight={self.weight}, status={self.status!r})"


class PotteryItemStore:
    """Хранилище изделий в памяти.

    Операции: добавление, получение по идентификатору, список.
    """

    def __init__(self):
        self._items = OrderedDict()
        self._counter = 0
        self._lock = threading.Lock()

    def add(self, item):
        """Добавить изделие, присвоив уникальный идентификатор.

        Возвращает идентификатор созданного изделия.
        """
        with self._lock:
            if item.name in self._items:
                raise ValueError(f"Изделие с названием {item.name!r} уже существует")
            self._counter += 1
            item_id = self._counter
            self._items[item_id] = item
            return item_id

    def get(self, item_id):
        """Получить изделие по идентификатору.

        Возвращает None, если изделие с таким идентификатором не существует.
        """
        with self._lock:
            return self._items.get(item_id)

    def list_items(self):
        """Вернуть список всех изделий в порядке добавления."""
        with self._lock:
            return list(self._items.values())

    def __len__(self):
        return len(self._items)
