from main import Account

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
        self.interest_rate = 0.005  # 0.5%
        self.withdrawal_limit = 700000

    def deposit(self, amount):
        result = super().deposit(amount)
        if "Deposited" in result:
            interest = amount * self.interest_rate
            self.balance += interest
            return f"{result} Interest added: {interest}. New balance is {self.balance}."
        return result

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            return f"Cannot withdraw more than {self.withdrawal_limit}."
        return super().withdraw(amount)

savings_account = SavingsAccount("SA12345", 10000)

print(savings_account.deposit(5000))
print("Savings Account Balance:", savings_account.get_balance())

print(savings_account.withdraw(1000))
print("Savings Account Balance:", savings_account.get_balance())

print(savings_account.withdraw(800000))
print("Savings Account Balance:", savings_account.get_balance())
