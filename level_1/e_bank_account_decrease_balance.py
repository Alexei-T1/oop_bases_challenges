"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income 
        return self.balance
    def decrease_balance(self, outcome: float):
        self.balance -= outcome
        if self.balance < 0:
            raise ValueError(f"balance cannot be negative.")
        return self.balance


if __name__ == '__main__':
    deposit = BankAccount('Gref', 100)
    print(deposit.balance)
    print(deposit.increase_balance(100))
    print(deposit.decrease_balance(100))
    print(deposit.decrease_balance(200))
