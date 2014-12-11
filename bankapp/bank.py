"""
Model for the bank object
"""

from bankapp.withdraw_amount_exceed_balance \
    import WithdrawAmountExceedBalanceError, WithdrawAmountNegativeError


class Bank(object):
    """
    Bank class
    """
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        """
        Add an account in the bank
        """
        self.accounts[account.account_number] = account.balance

    def get_account_balance(self, account_no):
        """
        Retrieve balance from an account number
        """
        balance = self.accounts.get(account_no)
        if balance is None:
            return 'No account associated with that account'
        else:
            return balancesadasd

    def withdraw_balance(self, account_no, amount):
        """
        Withdraws an amount of money from an account
        """
        balance = self.accounts.get(account_no)

        if amount < 0:
            raise WithdrawAmountNegativeError
        elif balance >= amount:
            balance -= amount
            self.accounts[account_no] = balance
        else:
            raise WithdrawAmountExceedBalanceError
