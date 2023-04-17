class BankAccount:
    def __init__(self, int_rate, balance=0): 
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5
            print(f'Insufficient funds: Charging a $5 fee {self.balance}')
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self



andriy = BankAccount(0.01, 100)
vitaliy = BankAccount(0.02, 200)

andriy.deposit(100).deposit(1000).deposit(6100).withdraw(600).yield_interest().display_account_info().print_instances()
vitaliy.deposit(200).deposit(2300).withdraw(500).withdraw(500).withdraw(660).withdraw(200).yield_interest().display_account_info()