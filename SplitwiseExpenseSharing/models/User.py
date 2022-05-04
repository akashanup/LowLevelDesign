from typing import Optional

from SplitwiseExpenseSharing.models.Account import Account


class User:
    account: Account
    youOwes: {Optional[int]: Optional[int]}
    owesYou: {Optional[int]: Optional[int]}

    def __init__(self, account: Account, youOwes=None, owesYou=None):
        if owesYou is None:
            owesYou = {}
        if youOwes is None:
            youOwes = {}
        self.account = account
        self.youOwes = youOwes
        self.owesYou = owesYou

    def showBalance(self) -> None:
        userIds = set(list(self.owesYou.keys()) + list(self.youOwes.keys()))
        balance = False
        for userId in userIds:
            if userId in self.owesYou and userId in self.youOwes:
                balance = self.owesYou[userId] - self.youOwes[userId]
                if balance > 0:
                    print(f"User {userId} ows {balance} to User {self.account.id}.")
                    balance = True
                elif balance < 0:
                    print(f"User {self.account.id} owes {-balance} to User {userId}.")
                    balance = True
                else:
                    del self.owesYou[userId]
                    del self.youOwes[userId]
            elif userId in self.owesYou:
                print(f"User {userId} ows {self.owesYou[userId]} to User {self.account.id}.")
                balance = True
            else:
                print(f"User {self.account.id} owes {self.youOwes[userId]} to User {userId}.")
                balance = True
        if not balance:
            print(f"No balances for {self.account.id}")
