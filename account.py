class BankAccount:
    """Represents one personal bank account."""

    def __init__(self, account_number, name, pin, balance=0.0):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount

    def verify_pin(self, pin):
        return self.pin == pin

    def change_pin(self, old_pin, new_pin):
        if not self.verify_pin(old_pin):
            raise ValueError("Incorrect old PIN.")
        if len(new_pin) != 4 or not new_pin.isdigit():
            raise ValueError("PIN must contain exactly 4 digits.")
        self.pin = new_pin
