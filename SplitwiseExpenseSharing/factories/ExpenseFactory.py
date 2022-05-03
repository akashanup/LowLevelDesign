from typing import Union, Optional

from SplitwiseExpenseSharing.exceptions.InvalidExpense import InvalidExpense
from SplitwiseExpenseSharing.models.EqualExpense import EqualExpense
from SplitwiseExpenseSharing.models.ExactExpense import ExactExpense
from SplitwiseExpenseSharing.models.Expense import Expense
from SplitwiseExpenseSharing.models.ExpenseType import ExpenseType
from SplitwiseExpenseSharing.models.PercentExpense import PercentExpense
from SplitwiseExpenseSharing.models.User import User


class ExpenseFactory:
    expenseType: str
    users: [User]
    totalAmount: float
    expenseAttributes: Optional[Union[int, float]]

    @staticmethod
    def buildExpense(expenseType: str, users: [User], totalAmount: float, expenseAttributes: Optional[Union[int, float]]) -> Expense:
        if expenseType == ExpenseType.EXACT.value:
            return Expense(ExactExpense(ExpenseType.EXACT, users, totalAmount, expenseAttributes))
        elif expenseType == ExpenseType.EQUAL.value:
            return Expense(EqualExpense(ExpenseType.EQUAL, users, totalAmount))
        elif expenseType == ExpenseType.PERCENT.value:
            return Expense(PercentExpense(ExpenseType.PERCENT, users, totalAmount, expenseAttributes))
        else:
            raise InvalidExpense

