from SplitwiseExpenseSharing.exceptions.InvalidExpenseException import InvalidExpenseException
from SplitwiseExpenseSharing.interfaces.IExpense import IExpense
from SplitwiseExpenseSharing.models.ExpenseType import ExpenseType
from SplitwiseExpenseSharing.models.User import User


class EqualExpense(IExpense):
    type: ExpenseType
    users: [User]
    totalAmount: float

    def __init__(self, expenseType: ExpenseType, users: [User], totalAmount: float) -> None:
        self.expense = expenseType
        self.users = users
        self.totalAmount = totalAmount

    def split(self) -> {User: float}:
        if not self.__validateSplit():
            raise InvalidExpenseException
        expense = {}
        for i in range(len(self.users)):
            expense[self.users[i]] = round(self.totalAmount / float(len(self.users)), 2)
        return expense

    def __validateSplit(self) -> bool:
        return len(self.users) > 0

