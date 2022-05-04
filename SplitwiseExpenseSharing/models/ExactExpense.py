from SplitwiseExpenseSharing.exceptions.InvalidExpenseException import InvalidExpenseException
from SplitwiseExpenseSharing.interfaces.IExpense import IExpense
from SplitwiseExpenseSharing.models.ExpenseType import ExpenseType
from SplitwiseExpenseSharing.models.User import User


class ExactExpense(IExpense):
    type: ExpenseType
    users: [User]
    totalAmount: float
    amounts: [float]

    def __init__(self, expenseType: ExpenseType, users: [User], totalAmount: float, amounts: [float]) -> None:
        self.expense = expenseType
        self.users = users
        self.totalAmount = totalAmount
        self.amounts = amounts

    def split(self) -> {User: float}:
        if not self.__validateSplit():
            raise InvalidExpenseException
        expense = {}
        for i in range(len(self.users)):
            expense[self.users[i]] = round(self.amounts[i], 2)
        return expense

    def __validateSplit(self) -> bool:
        return self.totalAmount == sum(self.amounts)


