class BankAccount:
    def __init__(self, name: str, balance: int):
        if balance < 0:
            raise ValueError("Balance can't be negative")

        self._name = name
        self._balance = balance

    def deposit(self, amount: int) -> int:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount
        return self._balance

    def withdraw(self, amount: int) -> int:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount
        return self._balance

    @property
    def balance(self) -> int:
        return self._balance

    def __repr__(self):
        return f"BankAccount(name={self._name}, balance={self._balance})"