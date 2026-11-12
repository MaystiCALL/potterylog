# === Stage 4: Связанная сущность ===
# Project: PotteryLog
def create_firing(product_id: int, name: str, temperature: int, glaze: str = None) -> dict:
    return {
        "id": generate_id(),
        "product_id": product_id,
        "name": name,
        "temperature": temperature,
        "glaze": glaze
    }


def add_firing(firings: list, product_id: int, name: str, temperature: int, glaze: str = None) -> dict:
    new_firing = create_firing(product_id, name, temperature, glaze)
    firings.append(new_firing)
    return new_firing


def generate_id() -> int:
    return len(_get_all_firings()) + 1


_get_all_firings = None


def _get_all_firings():
    return _get_all_firings.__wrapped__()


_get_all_firings.__wrapped__ = staticmethod(lambda: _load_firings())


def _load_firings():
    try:
        import json, os
        path = os.path.join(os.path.dirname(__file__), "firings.json")
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception:
        pass
    return []
