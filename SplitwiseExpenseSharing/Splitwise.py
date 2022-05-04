from typing import Union, Optional

from SplitwiseExpenseSharing.exceptions.InvalidCommandException import InvalidCommandException
from SplitwiseExpenseSharing.exceptions.InvalidExpenseException import InvalidExpenseException
from SplitwiseExpenseSharing.exceptions.InvalidUserException import InvalidUserException
from SplitwiseExpenseSharing.factories.ExpenseFactory import ExpenseFactory
from SplitwiseExpenseSharing.models.Account import Account
from SplitwiseExpenseSharing.models.Expense import Expense
from SplitwiseExpenseSharing.models.User import User
from SplitwiseExpenseSharing.models.UserShare import UserShare
from SplitwiseExpenseSharing.services.UserService import UserService


class Splitwise:
    users: dict[str, User]
    expenses: [Optional[Expense]]
    userShares: [Optional[UserShare]]

    def __init__(self):
        self.users = {}
        self.expenses = []
        self.userShares = []

    def addUser(self, userId: str, name: str, email: str, mobile: str) -> None:
        account = Account(userId, name, email, mobile)
        user = User(account)
        if userId not in self.users:
            self.users[userId] = user

    def __addExpense(self, payingUser: User, splittingUser: [User], totalAmount: float, expenseType: str,
                     expenseAttributes: [Union[int, float]] = None) -> Expense:
        expense = ExpenseFactory.buildExpense(payingUser, expenseType, splittingUser, totalAmount, expenseAttributes)
        self.expenses.append(expense)
        return expense

    def __addUserShare(self, userShares: [UserShare]) -> None:
        for userShare in userShares:
            self.userShares.append(userShare)

    @staticmethod
    def __splitExpense(expense: Expense) -> [UserShare]:
        return expense.split()

    def __showBalance(self, user: Optional[User] = None) -> None:
        if user:
            UserService.showBalance(self.userShares, user)
        else:
            for user in self.users.values():
                UserService.showBalance(self.userShares, user)

    def facilitate(self):
        while True:
            try:
                inp = input().strip().split(' ')
                inp[0] = inp[0].lower()
                if inp[0] == 'exit':
                    break
                if inp[0] == 'show':
                    if len(inp) == 1:
                        self.__showBalance()
                    else:
                        userId = inp[1]
                        if userId not in self.users:
                            raise InvalidUserException
                        searchedUser = self.users[userId]
                        self.__showBalance(searchedUser)
                elif inp[0] == 'expense':
                    # Find paying user.
                    userId = inp[1]
                    if userId not in self.users:
                        raise InvalidUserException

                    payingUser = self.users[userId]

                    # Find total amount.
                    totalAmount = float(inp[2])

                    # Find splitting users.
                    splittingUserCount = int(inp[3])
                    splittingUsers = []
                    inpIdx = 4
                    for i in range(splittingUserCount):
                        userId = inp[inpIdx]
                        if userId not in self.users:
                            raise InvalidUserException
                        splittingUsers.append(self.users[userId])
                        inpIdx += 1

                    # Find expense type
                    expenseType = inp[inpIdx].lower()
                    # Find expense attributes
                    expenseAttributes = [float(_) for _ in inp[inpIdx + 1:]]
                    expense = self.__addExpense(payingUser, splittingUsers, totalAmount, expenseType, expenseAttributes)
                    userShares = self.__splitExpense(expense)
                    self.__addUserShare(userShares)
                else:
                    raise InvalidCommandException
            except InvalidExpenseException:
                print("Invalid Expense. Please Retry!")
            except InvalidCommandException:
                print("Invalid Command. Please Retry!")
            except InvalidUserException:
                print("Invalid User. Please Retry!")
            except Exception as e:
                print("Something went wrong. Please Retry!")


splitWise = Splitwise()
splitWise.addUser('u1', 'Akash', 'akash@gmail.com', '9999988888')
splitWise.addUser('u2', 'Damon', 'damon@gmail.com', '8888877777')
splitWise.addUser('u3', 'Klaus', 'klaus@gmail.com', '7777766666')
splitWise.addUser('u4', 'Stefan', 'stefan@gmail.com', '6666655555')
splitWise.facilitate()
