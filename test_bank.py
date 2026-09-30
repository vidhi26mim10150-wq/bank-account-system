import unittest
from bank.account import BankAccount
from bank.analytics import financial_summary

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("1234567890", "Test User", "1234", 10000)

    def test_deposit(self):
        self.account.deposit(5000)
        self.assertEqual(self.account.balance, 15000)

    def test_withdraw(self):
        self.account.withdraw(2000)
        self.assertEqual(self.account.balance, 8000)

    def test_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(20000)

    def test_pin(self):
        self.assertTrue(self.account.verify_pin("1234"))
        self.assertFalse(self.account.verify_pin("9999"))

    def test_financial_summary(self):
        transactions = [
            {"type": "Deposit", "amount": 5000},
            {"type": "Withdrawal", "amount": 1000},
            {"type": "Transfer", "amount": 500},
        ]
        summary = financial_summary(transactions)
        self.assertEqual(summary["total_deposits"], 5000)
        self.assertEqual(summary["total_withdrawals"], 1500)
        self.assertEqual(summary["transaction_count"], 3)

if __name__ == "__main__":
    unittest.main()
