class Account:
    def __init__(self, balance=0):
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self._balance


class SavingsAccount(Account):
    def __init__(self, balance=0):
        super().__init__(balance)
        self._interest_rate = 0.005
        self._withdrawal_limit = 700000

    def deposit(self, amount):
        if amount > 0:
            super().deposit(amount)
            self._balance += amount * self._interest_rate
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self._withdrawal_limit:
            super().withdraw(amount)
        else:
            print(f"Cannot withdraw more than {self._withdrawal_limit}")


savings_account = SavingsAccount(10000)

savings_account.deposit(5000)
print("Savings Account Balance:", savings_account.get_balance())
savings_account.withdraw(1000)
print("Savings Account Balance:", savings_account.get_balance())

