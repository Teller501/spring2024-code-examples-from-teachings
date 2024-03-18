class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author


# EX 1: Bank Exercise

class Account:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return f"{self.account_number} - {self.owner} - {self.balance}"


class Customer:
    def __init__(self, name, address, email, phone_number):
        self.name = name
        self.address = address
        self.email = email
        self.phone_number = phone_number

    def __str__(self) -> str:
        return f"{self.name} - {self.email} - {self.phone_number} - {self.address}"


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account


customer = Customer('Åge Bent', '123 Main St', 51515151,
                    'anders.teller@mail.dk')
customer2 = Customer('Klaus Johansen', '123 Main St', 51515151,
                     'dsadsa@mail.dk')
customer3 = Customer('Anders Iversen', '123 Main St', 51515151,
                     'dsadsa@mail.dk')


account = Account('123456', customer, 200.0)
account2 = Account('123457', customer2, 109.0)
account3 = Account('123458', customer3, 800.0)

bank = Bank('My Bank')
for acc in [account, account2, account3]:
    bank.add_account(acc)


# EX 2: Sorting the Customers
customer_name_sort = sorted(
    [customer, customer2, customer3], key=lambda x: x.name)

print('Sorted Customers')

for c in customer_name_sort:
    print(c)

account_balance_sorted = sorted(
    [account, account2, account3], key=lambda x: x.balance)

print('Sorted Balance')

for a in account_balance_sorted:
    print(a)

# Sort based on Customer (not name) and then on the amount. (hint: return a tuple)

account_customer_sorted = sorted(
    [account, account2, account3], key=lambda x: (x.owner.name, x.balance))

print('Sorted Customer and Balance')

for a in account_customer_sorted:
    print(a)
