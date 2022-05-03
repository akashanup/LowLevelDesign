from typing import Optional

from SplitwiseExpenseSharing.models.Account import Account


class User:
    account: Account
    youOws: {Optional[int]: Optional[int]}
    owsYou: {Optional[int]: Optional[int]}

    def __init__(self, account: Account, youOws=None, owsYou=None):
        if owsYou is None:
            owsYou = {}
        if youOws is None:
            youOws = {}
        self.account = account
        self.youOws = youOws
        self.owsYou = owsYou

    def showBalance(self) -> None:
        userIds = set(list(self.owsYou.keys()) + list(self.youOws.keys()))
        balance = False
        for userId in userIds:
            if userId in self.owsYou and userId in self.youOws:
                balance = self.owsYou[userId] - self.youOws[userId]
                if balance > 0:
                    print(f"User {userId} ows {balance} to User {self.account.id}.")
                    balance = True
                elif balance < 0:
                    print(f"User {self.account.id} owes {-balance} to User {userId}.")
                    balance = True
                else:
                    del self.owsYou[userId]
                    del self.youOws[userId]
            elif userId in self.owsYou:
                print(f"User {userId} ows {self.owsYou[userId]} to User {self.account.id}.")
                balance = True
            else:
                print(f"User {self.account.id} owes {self.youOws[userId]} to User {userId}.")
                balance = True
        if not balance:
            print(f"No balances for {self.account.id}")
