from typing import Union, Optional

from SplitwiseExpenseSharing.exceptions.InvalidExpense import InvalidExpense
from SplitwiseExpenseSharing.factories.ExpenseFactory import ExpenseFactory
from SplitwiseExpenseSharing.models.Account import Account
from SplitwiseExpenseSharing.models.User import User
from SplitwiseExpenseSharing.models.UserExpense import UserExpense


class Splitwise:
    users: [Optional[User]]
    userExpenses: [Optional[UserExpense]]

    def __init__(self):
        self.users = []
        self.userExpenses = []

    def addUser(self, userId: str, name: str, email: str, mobile: str) -> None:
        account = Account(userId, name, email, mobile)
        user = User(account)
        self.users.append(user)

    def __addExpense(self, payingUser: User, splittingUser: [User], totalAmount: float, expenseType: str,
                     expenseAttributes: [Union[int, float]] = None) -> None:
        expense = ExpenseFactory.buildExpense(expenseType, splittingUser, totalAmount, expenseAttributes)
        # Add the expense to the payingUser's expenses because he was a part of it.
        userExpense = UserExpense(payingUser, expense)
        self.userExpenses.append(userExpense)

        splitExpense = expense.type.split()
        for user, amount in splitExpense.items():
            if user is not payingUser:
                # Add the expense to the user's expenses because he was a part of it.
                userExpense = UserExpense(user, expense)
                self.userExpenses.append(userExpense)

                # Since payingUser has paid for this expense so, splitUser must owe an amount to him for this transaction.
                if payingUser.account.id in user.youOws:
                    user.youOws[payingUser.account.id] += amount
                else:
                    user.youOws[payingUser.account.id] = amount
                if user.account.id in payingUser.owsYou:
                    payingUser.owsYou[user.account.id] += amount
                else:
                    payingUser.owsYou[user.account.id] = amount

    def __showBalance(self, user: Optional[User] = None) -> None:
        if user:
            user.showBalance()
        else:
            for user in self.users:
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
                    searchedUser = None
                    for user in self.users:
                        if user.account.id == userId:
                            searchedUser = user
                            break
                    self.__showBalance(searchedUser)
            else:
                # Find paying user.
                userId = inp[1]
                payingUser = None
                for user in self.users:
                    if user.account.id == userId:
                        payingUser = user
                        break

                # Find total amount.
                totalAmount = float(inp[2])

                # Find splitting users.
                splittingUserCount = int(inp[3])
                splittingUsers = []
                inpIdx = 4
                for i in range(splittingUserCount):
                    userId = inp[inpIdx]
                    for user in self.users:
                        if user.account.id == userId:
                            splittingUsers.append(user)
                            break
                    inpIdx += 1

                # Find expense type
                expenseType = inp[inpIdx]
                # Find expense attributes
                expenseAttributes = [float(_) for _ in inp[inpIdx + 1:]]
                try:
                    self.__addExpense(payingUser, splittingUsers, totalAmount, expenseType, expenseAttributes)
                except InvalidExpense:
                    print("Invalid Expense. Please Retry!")



splitWise = Splitwise()
splitWise.addUser('u1', 'Akash', 'akash@gmail.com', '9999988888')
splitWise.addUser('u2', 'Damon', 'damon@gmail.com', '8888877777')
splitWise.addUser('u3', 'Klaus', 'klaus@gmail.com', '7777766666')
splitWise.addUser('u4', 'Stefan', 'stefan@gmail.com', '6666655555')
splitWise.facilitate()
