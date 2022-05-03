# Tic Tac Toe - NxN

### Problem Statement
Let's look at the game of Tic Tac Toe. Tic Tac Toe is a two-player strategy game generally played on a 3*3 grid. 
There are 9 empty cells and 9 pieces - 5 pieces of 'X' and 4 pieces of 'O'

The game starts with an empty grid.

### Rules of the game
- The game is played between two players. One player owns the X pieces and can put it on any of the empty cells in the grid. The other player owns the O pieces and can in any of the empty cells.
- The player with X makes the first turn. Each player plays alternately after that.
- The first player to form a horizontal/vertical/diagonal sequence wins.

### Requirements
Create a command-line application for tic tac toe with the following requirements:

- Ask the user for the names of the two players
- Print the grid after initializing
- Allow the user to make moves on behalf of both the players.
  - The user will make a move by entering the cell position.
  - You need to determine the piece (X/O) and make the move if it is valid.
  - Valid move:
    - The piece is controlled by the player having the current turn
    - The cell is empty
  - If the move is invalid
    - print 'Invalid Move'
    - the same player plays again
  - If the move is valid:
    - put the piece on the cell
    - print the board after the move
- Determine if a player has won or if there are no valid moves left. Ignore all moves mentioned after that.

### Note
A position in the cell is represented by two values: row number (1-3) and column number (1-3).

Examples:
- 3 1 represents the cell at the extreme bottom-left (3rd row, 1st column)
- 1 3 represents the cell at the extreme top-right (1st row, 3rd column)

### Input/Output Format
The code should strictly follow the input/output format and will be tested with provided test cases.

### Input Format
Multiple lines with each line containing the Cell Position. The row and column numbers will be separated by a space.

Stop taking the input when you encounter the word exit.

### Output Format
Print the initial grid. This would be followed by the grid after each move. In case of an invalid move, do not print the grid and instead print:
- Invalid Move

The board needs to be printed in the following format based on the respective position:
```sh
X X O
- - X
O O -
```
Here,

X and O represent the different pieces. An empty cell is represented by a hyphen (-).

The initial position of the board would be:
```sh
- - -
- - -
- - -
```
**If the player wins after a move, print: 'Player_Name won the game'**

**If there are no valid moves left for any player, print 'Game Over'**

### Example 1
**Sample Input**
```sh
X Damon
O Stefan
2 2
1 3
1 1
1 2
2 2
3 3
exit
```
**Sample Output**
```sh
- - -
- - -
- - -
- - -
- X -
- - -
- - O
- X -
- - -
X - O
- X -
- - -
X O O
- X -
- - -
Invalid Move
X O O
- X -
- - X
Damon won the game
```

### Example 2
**Sample Input**
```sh
X Damon
O Stefan
2 3
1 2
2 2
2 1
1 1
3 3
3 2
3 1
1 3
exit
```
**Sample Output**
```sh
- - -
- - -
- - -
- - -
- - X
- - -
- O -
- - X
- - -
- O -
- X X
- - -
- O -
O X X
- - -
X O -
O X X
- - -
X O -
O X X
- - O
X O -
O X X
- X O
X O X
O X X
O X O
Game Over
```

### Example 3
**Sample Input**
```sh
X Damon
O Stefan
exit
```
**Sample Output**
```sh
- - -
- - -
- - -
```

### Expectations
- Make sure that you have a working and demonstrable code
- Make sure that the code is functionally correct
- Code should be modular and readable
- Separation of concern should be addressed
- Please do not write everything in a single file (if not coding in C/C++)
- Code should easily accommodate new requirements and minimal changes
- There should be a main method from where the code could be easily testable
- [Optional] Write unit tests, if possible
- No need to create a GUI

### Optional Requirements
Please do these only if you’ve time left. You can write your code such that these could be accommodated without changing your code much.

- Keep the code extensible to change the size of the grid.
- Keep the code extensible to allow different types of pieces.
- Keep the code extensible to allow more than 2 players/piece types.
