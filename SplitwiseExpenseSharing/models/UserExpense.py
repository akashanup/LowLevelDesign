from SplitwiseExpenseSharing.models.Expense import Expense
from SplitwiseExpenseSharing.models.User import User


class UserExpense:
    user: User
    expense: Expense

    def __init__(self, user: User, expense: Expense) -> None:
        self.user = user
        self.expense = expense
