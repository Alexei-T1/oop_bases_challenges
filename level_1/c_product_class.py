"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, type: str, weight: int, unit: str):
        self.type = type
        self.weight = weight
        self.unit = unit


if __name__ == '__main__':
    prod = Product('Solt', 5, 'kg')
    print(f'Информация о продукте: {prod.type}, {prod.weight}, {prod.unit}')
