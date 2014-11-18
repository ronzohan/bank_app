class Account(object):
    def __init__(self, account_number, balance):
        self.account_number = account_number

        if type(balance) == int:
            self.balance = balance
        else:
            raise TypeError("Balance is of {}, must be int".format(
                type(balance)))
