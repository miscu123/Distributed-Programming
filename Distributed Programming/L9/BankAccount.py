class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Soldul initial e negativ")
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Suma pentru depunere trebuie sa fie > 0")
            return False
        self.__balance += amount
        print("Depunere reusita: ", amount)
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Suma pentru retragere trebuie sa fie > 0")
            return False
        if amount > self.__balance:
            print("Fonduri insuficiente!")
            return False
        self.__balance -= amount
        print("Retragere reusita: ", amount)
        return True

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
print("Sold initial: ", account.get_balance())
account.deposit(500)
account.withdraw(200)
print("Sold final: ", account.get_balance())