# Splitwise

### Problem Statement
Create an expense sharing application.

An expense sharing application is where you can add your expenses and split it among different people. The app keeps balances between people as in who owes how much to whom.

### Requirements
- User: Each user should have a userId, name, email, mobile number.
- Expense: Could either be EQUAL, EXACT or PERCENT
- Users can add any amount, select any type of expense and split with any of the available users.
- The percent and amount provided could have decimals upto two decimal places.
- In case of percent, you need to verify if the total sum of percentage shares is 100 or not.
- In case of exact, you need to verify if the total sum of shares is equal to the total amount or not.
- The application should have a capability to show expenses for a single user as well as balances for everyone.
- When asked to show balances, the application should show balances of a user with all the users where there is a non-zero balance.
- The amount should be rounded off to two decimal places. Say if User1 paid 100 and amount is split equally among 3 people. Assign 33.34 to first person and 33.33 to others.

### Input Format
- You can create a few users in your main method. No need to take it as input.
- There will be 3 types of input:
  - Expense in the format: EXPENSE <user-id-of-person-who-paid> <no-of-users> <space-separated-list-of-users> <EQUAL/EXACT/PERCENT> <space-separated-values-in-case-of-non-equal>
  - Show balances for all: SHOW
  - Show balances for a single user: SHOW <user-id>

### Output Format
- When asked to show balance for a single user. Show all the balances that user is part of:
- Format: <user-id-of-x> owes <user-id-of-y>: <amount>
- If there are no balances for the input, print No balances
- In cases where the user for which balance was asked for, owes money, they’ll be x. They’ll be y otherwise.

### Example 1
**Sample Input**
```sh
SHOW
SHOW u1
EXPENSE u1 1000 4 u1 u2 u3 u4 EQUAL
SHOW u4
SHOW u1
EXPENSE u1 1250 2 u2 u3 EXACT 370 880
SHOW
EXPENSE u4 1200 4 u1 u2 u3 u4 PERCENT 40 20 20 20
SHOW u1
SHOW
```
**Sample Output**
```sh
No balances
No balances
User4 owes User1: 250
User2 owes User1: 250
User3 owes User1: 250
User4 owes User1: 250
User2 owes User1: 620
User3 owes User1: 1130
User4 owes User1: 250
User1 owes User4: 230
User2 owes User1: 620
User3 owes User1: 1130
User1 owes User4: 230
User2 owes User1: 620
User2 owes User4: 240
User3 owes User1: 1130
User3 owes User4: 240
```

### Expectations
- Make sure that you have a working and demonstrable code
- Make sure that the code is functionally correct
- Code should be modular and readable
- Separation of concern should be addressed
- Please do not write everything in a single file
- Code should easily accommodate new requirements and minimal changes
- There should be a main method from where the code could be easily testable
- [Optional] Write unit tests, if possible
- No need to create a GUI

### Optional Requirements
Please do these only if you’ve time left. You can write your code such that these could be accommodated without changing your code much.

- A way to add an expense name while adding the expense. Can also add notes, images, etc.
- Option to split by share. Ex: ‘User4 pays and everyone splits equally. You pay for 2 people.’ could be added as: u4 1200 4 u1 u2 u3 u4 SHARE 2 1 1 1
- A way to show the passbook for a user. The entries should show all the transactions a user was part of. You can print in any format you like.
- There can be an option to simplify expenses. When simplify expenses is turned on (is true), the balances should get simplified. Ex: ‘User1 owes 250 to User2 and User2 owes 200 to User3’ should simplify to ‘User1 owes 50 to User2 and 200 to User3’.
