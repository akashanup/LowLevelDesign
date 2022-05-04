from typing import Union

from SplitwiseExpenseSharing.models.EqualExpense import EqualExpense
from SplitwiseExpenseSharing.models.ExactExpense import ExactExpense
from SplitwiseExpenseSharing.models.PercentExpense import PercentExpense
from SplitwiseExpenseSharing.models.User import User


class Expense:
    payingUser: User
    type: Union[ExactExpense, EqualExpense, PercentExpense]

    def __init__(self, payingUser: User, expenseType: Union[ExactExpense, EqualExpense, PercentExpense]) -> None:
        self.payingUser = payingUser
        self.type = expenseType
