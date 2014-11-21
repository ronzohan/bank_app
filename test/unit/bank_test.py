import unittest
from bank import Bank
from account import Account
from withdraw_amount_exceed_balance \
    import WithdrawAmountExceedBalanceError, WithdrawAmountNegativeError


class TestBank(unittest.TestCase):
    def test_add_account(self):
        bank = Bank()

        account_1 = Account("001", 50)
        account_2 = Account("002", 20)

        bank.add_account(account_1)
        bank.add_account(account_2)

        self.assertEqual(len(bank.accounts), 2)

    def test_get_account_balance(self):
        bank = Bank()

        account_1 = Account("001", 50)

        bank.add_account(account_1)

        self.assertEqual(bank.get_account_balance("001"), 50)

    def test_account_number_exists(self):
        bank = Bank()
        self.assertEqual(bank.get_account_balance("002"), 'No account associated with that account')

    def test_account_withdraw_balance(self):
        bank = Bank()
        account_1 = Account("001", 50)

        bank.add_account(account_1)
        bank.withdraw_balance("001", 50)

        self.assertEqual(bank.get_account_balance("001"), 0)

    def test_account_withdraw_amount_exceeds_balance(self):
        bank = Bank()
        account_1 = Account("001", 50)

        bank.add_account(account_1)

        self.assertRaises(WithdrawAmountExceedBalanceError,
                          bank.withdraw_balance, "001", 100)

    def test_account_withdraw_negative_amount(self):
        bank = Bank()
        account_1 = Account("001", 50)

        bank.add_account(account_1)

        self.assertRaises(WithdrawAmountNegativeError, bank.withdraw_balance,
                          "001", -1)
