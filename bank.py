from withdraw_amount_exceed_balance \
    import WithdrawAmountExceedBalanceError, WithdrawAmountNegativeError


class Bank(object):
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account.balance

    def get_account_balance(self, account_no):
        try:
            return self.accounts[account_no]
        except:
            raise KeyError

    def withdraw_balance(self, account_no, amount):
        balance = self.accounts[account_no]

        if amount < 0:
            raise WithdrawAmountNegativeError
        elif balance >= amount:
            balance -= amount
            self.accounts[account_no] = balance
        else:
            raise WithdrawAmountExceedBalanceError
