from SplitwiseExpenseSharing.models.User import User


class UserShare:
    payingUser: User
    paidForUser: User
    amount: float

    def __init__(self, payingUser: User, paidForUser: User, amount: float):
        self.payingUser = payingUser
        self.paidForUser = paidForUser
        self.amount = amount
