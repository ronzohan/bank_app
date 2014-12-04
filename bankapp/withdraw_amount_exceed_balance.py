"""
Classes of errors
"""

class WithdrawAmountExceedBalanceError(Exception):
    """
    Error for withdrawing amount more than the balance
    """
    pass

class WithdrawAmountNegativeError(Exception):
    """
    Error for withdrawing negative amount
    """
    pass
