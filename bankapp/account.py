"""
Model for Account object
"""
class Account(object):
    """
    Account object used by the Bank
    """
    def __init__(self, account_number, balance):
        self.account_number = account_number

        if type(balance) == int:
            self.balance = balance
        else:
            try:
                self.balance = int(balance)
            except:
                raise TypeError("Balance is of {}, must be int".format(
                    type(balance)))

