# Create account class with 2 attributes - balance and balance_no
# create methods for credit , debit and printing the balance

class Account:

    def __init__(self, balance, balance_no):
        self.balance = balance
        self.balance_no = balance_no

    def credit(self, amount):
        self.balance += amount
        print("Credited:", amount)
        print("Current balance:", self.balance)

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Debited:", amount)
            print("Current balance:", self.balance)

    def print_balance(self):
        print("Account number:", self.balance_no)
        print("Current balance:", self.balance)


a1 = Account(5000, 12345)

a1.print_balance()

a1.credit(2000)

a1.debit(1500)

a1.print_balance()