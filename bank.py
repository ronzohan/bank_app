class Bank(object):
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account.balance

    def get_account_balance(self, account_no):
        if self.accounts[account_no]:
            balance = self.accounts[account_no]
        else:
            raise KeyError
        return balance
