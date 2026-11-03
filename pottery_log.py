# === Stage 1: Каркас модуля ===
# Project: PotteryLog
from dataclasses import dataclass, field
from typing import List


@dataclass
class Product:
    name: str
    clay_type: str
    weight: float
    status: str = "в работе"


def make_demo_records() -> List[Product]:
    return [
        Product("Кружка", "керамическая", 250.0, "готово"),
        Product("Ваза", "глиняная", 1800.0, "в работе"),
        Product("Тарелка", "фарфоровая", 320.0, "спечён"),
        Product("Миска", "керамическая", 410.0, "сушится"),
    ]


def main() -> None:
    records = make_demo_records()
    print("Демонстрационные изделия мастерской:")
    for i, product in enumerate(records, start=1):
        print(f"{i}. {product.name} ({product.clay_type}, "
              f"{product.weight} г, {product.status})")


if __name__ == "__main__":
    main()
