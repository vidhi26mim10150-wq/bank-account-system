from datetime import datetime

class Transaction:
    """Stores information about one transaction."""

    def __init__(self, transaction_type, amount, balance_after, description=""):
        self.transaction_type = transaction_type
        self.amount = float(amount)
        self.balance_after = float(balance_after)
        self.description = description
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "type": self.transaction_type,
            "amount": self.amount,
            "balance_after": self.balance_after,
            "description": self.description,
            "date": self.date,
        }
