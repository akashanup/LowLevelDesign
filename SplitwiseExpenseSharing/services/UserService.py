from SplitwiseExpenseSharing.models.UserShare import UserShare
from SplitwiseExpenseSharing.models.User import User


class UserService:
    @staticmethod
    def showBalance(userShares: [UserShare], user: User):
        # Process balances.
        hashmap = {}
        for userShare in userShares:
            if userShare.payingUser is user:
                if userShare.paidForUser in hashmap:
                    hashmap[userShare.paidForUser] += userShare.amount
                else:
                    hashmap[userShare.paidForUser] = userShare.amount
            if userShare.paidForUser is user:
                if userShare.payingUser in hashmap:
                    hashmap[userShare.payingUser] -= userShare.amount
                else:
                    hashmap[userShare.payingUser] = -userShare.amount

        # Print Balances.
        balance = False
        for userShare, amount in hashmap.items():
            if amount > 0:
                print(f"User {userShare.account.id} owes {amount} to User {user.account.id}.")
                balance = True
            elif amount < 0:
                print(f"User {user.account.id} owes {-amount} to User {userShare.account.id}.")
                balance = True

        if not balance:
            print(f"No balances for {user.account.id}")
        print()
