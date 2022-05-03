from typing import Union

from SplitwiseExpenseSharing.models.EqualExpense import EqualExpense
from SplitwiseExpenseSharing.models.ExactExpense import ExactExpense
from SplitwiseExpenseSharing.models.PercentExpense import PercentExpense


class Expense:
    type: Union[ExactExpense, EqualExpense, PercentExpense]

    def __init__(self, expenseType: Union[ExactExpense, EqualExpense, PercentExpense]) -> None:
        self.type = expenseType
