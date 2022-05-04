from typing import Union

from SplitwiseExpenseSharing.models.EqualExpense import EqualExpense
from SplitwiseExpenseSharing.models.ExactExpense import ExactExpense
from SplitwiseExpenseSharing.models.PercentExpense import PercentExpense
from SplitwiseExpenseSharing.models.User import User
from SplitwiseExpenseSharing.models.UserShare import UserShare


class Expense:
    payingUser: User
    type: Union[ExactExpense, EqualExpense, PercentExpense]

    def __init__(self, payingUser: User, expenseType: Union[ExactExpense, EqualExpense, PercentExpense]) -> None:
        self.payingUser = payingUser
        self.type = expenseType

    def split(self) -> [UserShare]:
        splitShares = self.type.split()
        userShares = []
        for user, amount in splitShares.items():
            userShares.append(UserShare(self.payingUser, user, amount))
        return userShares
