from withdraw_amount_exceed_balance \
    import WithdrawAmountExceedBalanceError, WithdrawAmountNegativeError


class Bank(object):
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account.balance

    def get_account_balance(self, account_no):
        balance = self.accounts.get(account_no)
        if balance is None:
            return 'No account associated with that account'
        else:
            return balance

    def withdraw_balance(self, account_no, amount):
        balance = self.accounts.get(account_no)

        if amount < 0:
            raise WithdrawAmountNegativeError
        elif balance >= amount:
            balance -= amount
            self.accounts[account_no] = balance
        else:
            raise WithdrawAmountExceedBalanceError
