from SplitwiseExpenseSharing.models.Account import Account


class User:
    account: Account

    def __init__(self, account: Account):
        self.account = account
