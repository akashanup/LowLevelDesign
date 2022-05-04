from SplitwiseExpenseSharing.models.User import User


class UserShareService:

    @staticmethod
    def update(payingUser: User, splitExpense: {User: float}) -> None:
        for user, amount in splitExpense.items():
            if user is not payingUser:
                # Since payingUser has paid for this expense so, splitUser must owe an amount to him for this transaction.
                if payingUser.account.id in user.youOwes:
                    user.youOwes[payingUser.account.id] += amount
                else:
                    user.youOwes[payingUser.account.id] = amount
                if user.account.id in payingUser.owesYou:
                    payingUser.owesYou[user.account.id] += amount
                else:
                    payingUser.owesYou[user.account.id] = amount

