from typing import Union, Optional

from SplitwiseExpenseSharing.exceptions.InvalidExpense import InvalidExpense
from SplitwiseExpenseSharing.factories.ExpenseFactory import ExpenseFactory
from SplitwiseExpenseSharing.models.Account import Account
from SplitwiseExpenseSharing.models.Expense import Expense
from SplitwiseExpenseSharing.models.User import User
from SplitwiseExpenseSharing.services.UserShareService import UserShareService


class Splitwise:
    users: dict[str, User]
    expenses: [Optional[Expense]]

    def __init__(self):
        self.users = {}
        self.expenses = []

    def addUser(self, userId: str, name: str, email: str, mobile: str) -> None:
        account = Account(userId, name, email, mobile)
        user = User(account)
        if userId not in self.users:
            self.users[userId] = user

    def __addExpense(self, payingUser: User, splittingUser: [User], totalAmount: float, expenseType: str,
                     expenseAttributes: [Union[int, float]] = None) -> Expense:
        expense = ExpenseFactory.buildExpense(expenseType, splittingUser, totalAmount, expenseAttributes)
        self.expenses.append(expense)
        return expense

    @staticmethod
    def __splitExpense(expense: Expense) -> {User: float}:
        return expense.type.split()

    def __showBalance(self, user: Optional[User] = None) -> None:
        if user:
            user.showBalance()
        else:
            for user in self.users.values():
                user.showBalance()
                print()

    def facilitate(self):
        while True:
            inp = input().strip().split(' ')
            if inp[0] == 'Exit':
                break
            if inp[0] == 'Show':
                if len(inp) == 1:
                    self.__showBalance()
                else:
                    userId = inp[1]
                    searchedUser = self.users[userId]
                    self.__showBalance(searchedUser)
            else:
                # Find paying user.
                userId = inp[1]
                payingUser = self.users[userId]

                # Find total amount.
                totalAmount = float(inp[2])

                # Find splitting users.
                splittingUserCount = int(inp[3])
                splittingUsers = []
                inpIdx = 4
                for i in range(splittingUserCount):
                    userId = inp[inpIdx]
                    splittingUsers.append(self.users[userId])
                    inpIdx += 1

                # Find expense type
                expenseType = inp[inpIdx]
                # Find expense attributes
                expenseAttributes = [float(_) for _ in inp[inpIdx + 1:]]
                try:
                    expense = self.__addExpense(payingUser, splittingUsers, totalAmount, expenseType, expenseAttributes)
                    splitExpense = self.__splitExpense(expense)
                    UserShareService.update(payingUser, splitExpense)
                except InvalidExpense:
                    print("Invalid Expense. Please Retry!")


splitWise = Splitwise()
splitWise.addUser('u1', 'Akash', 'akash@gmail.com', '9999988888')
splitWise.addUser('u2', 'Damon', 'damon@gmail.com', '8888877777')
splitWise.addUser('u3', 'Klaus', 'klaus@gmail.com', '7777766666')
splitWise.addUser('u4', 'Stefan', 'stefan@gmail.com', '6666655555')
splitWise.facilitate()
