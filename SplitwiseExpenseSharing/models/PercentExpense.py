from SplitwiseExpenseSharing.exceptions.InvalidExpenseException import InvalidExpenseException
from SplitwiseExpenseSharing.interfaces.IExpense import IExpense
from SplitwiseExpenseSharing.models.ExpenseType import ExpenseType
from SplitwiseExpenseSharing.models.User import User


class PercentExpense(IExpense):
    type: ExpenseType
    users: [User]
    totalAmount: float
    percentages: [int]

    def __init__(self, expenseType: ExpenseType, users: [User], totalAmount: float, percentages: [int]) -> None:
        self.expense = expenseType
        self.users = users
        self.totalAmount = totalAmount
        self.percentages = percentages

    def split(self) -> {User: float}:
        if not self.__validateSplit():
            raise InvalidExpenseException
        expense = {}
        for i in range(len(self.users)):
            expense[self.users[i]] = round(self.totalAmount * (self.percentages[i] / 100.0), 2)
        return expense

    def __validateSplit(self) -> bool:
        return 100 == sum(self.percentages)
