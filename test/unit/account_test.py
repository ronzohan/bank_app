import unittest
from account import Account


class TestAccount(unittest.TestCase):
    def test_account_object_returns_current_balance(self):
        account = Account(001, 50)
        self.assertEqual(account.account_number, 001)
        self.assertEqual(account.balance, 50)

