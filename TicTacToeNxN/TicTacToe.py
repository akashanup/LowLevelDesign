from typing import Optional

from TicTacToeNxN.exceptions.InvalidMoveException import InvalidMoveException
from TicTacToeNxN.factories.PieceFactory import PieceFactory
from TicTacToeNxN.models import account as accountModel
from TicTacToeNxN.models import board as boardModel
from TicTacToeNxN.models import cell as cellModel
from TicTacToeNxN.models import cellPosition as cellPositionModel
from TicTacToeNxN.models import gameStatuse as gameStatusModel
from TicTacToeNxN.models import move as moveModel
from TicTacToeNxN.models import piece as pieceModel
from TicTacToeNxN.models import player as playerModel
from TicTacToeNxN.models import pieceType as pieceTypeModel


class TicTacToe:
    size: int
    board: boardModel.Board
    players: [playerModel.Player]
    currentPlayerIdx: int
    moves: [moveModel.Move]
    status: gameStatusModel.GameStatus

    def __init__(self, size: Optional[int] = 3):
        self.size = size
        self.board = self.__initializeBoard()
        self.players = self.__initializePlayers()
        self.currentPlayerIdx = 0
        self.moves = []
        self.status = gameStatusModel.GameStatus.NOT_STARTED
        self.__printBoard()

    def __initializeBoard(self) -> boardModel.Board:
        cells = []
        for r in range(self.size):
            for c in range(self.size):
                cellPosition = cellPositionModel.CellPosition(r, c)
                piece = PieceFactory.buildPiece()
                cell = cellModel.Cell(piece, cellPosition)
                cells.append(cell)
        return boardModel.Board(self.size, cells)

    def __initializePlayers(self) -> [playerModel.Player]:
        totalPieces = self.size ** 2
        playerPiecesCount = [0, 0]
        playerPiecesCount[0] = (totalPieces // 2) + 1
        playerPiecesCount[1] = totalPieces - playerPiecesCount[0]
        players = []
        for i in range(2):
            pieceIdentifier, playerName = input().strip().split(' ')
            account = accountModel.Account(playerName)
            pieces = []
            for j in range(playerPiecesCount[i]):
                pieces.append(PieceFactory.buildPiece(pieceIdentifier))
            player = playerModel.Player(account, pieceTypeModel.PieceType.getIdentifier(pieceIdentifier), pieces)
            players.append(player)
        return players

    def play(self) -> None:
        while True:
            inp = input().strip().split(' ')
            if inp[0] == 'exit':
                self.__exitGame()
                break
            # Flow:
            #   1. Print Board
            #   2. Validate the move
            #   3. Make the move
            #   4. Check for winner or Game Over
            #   5. Change Turn
            position = cellPositionModel.CellPosition(int(inp[0])-1, int(inp[1])-1)
            try:
                player = self.players[self.currentPlayerIdx]
                move = moveModel.Move(player, player.pieces[-1], position)
                if self.__validateMove(move):
                    self.__makeMove(move)
                    self.__printBoard()
                    winnerPiece = self.__checkForWinner()
                    if winnerPiece:
                        self.__processWinner(winnerPiece)
                        self.__endGame()
                        break
                    elif self.__checkForGameOver():
                        print("Game Over")
                        self.__endGame()
                        break
                    else:
                        self.__changePlayerTurn()
                else:
                    print("Invalid Move")
                    print()
            except InvalidMoveException:
                print("Invalid Move")
                print()
            except Exception as e:
                # print("Oops!", e.__class__, "occurred.")
                print("Something Went Wrong! Please  Try Again.")
                print()

    def __validateMove(self, move: moveModel.Move) -> bool:
        return move.validate(self.board)

    def __makeMove(self, move: moveModel.Move) -> None:
        move.make(self.board)
        self.moves.append(move)

    def __printBoard(self) -> None:
        self.board.printCurrentState()

    def __checkForWinner(self) -> [pieceModel.Piece]:
        return self.board.checkForWinner()

    def __processWinner(self, piece: pieceModel.Piece) -> None:
        for player in self.players:
            if player.pieceIdentifier == piece:
                print(f"{player.account.name} has won the game")
                break

    def __checkForGameOver(self) -> bool:
        return self.board.checkForGameOver()

    def __changePlayerTurn(self) -> None:
        self.currentPlayerIdx = (self.currentPlayerIdx + 1) % len(self.players)

    def __startGame(self) -> None:
        self.status = gameStatusModel.GameStatus.ACTIVE

    def __endGame(self) -> None:
        self.status = gameStatusModel.GameStatus.ENDED

    def __exitGame(self) -> None:
        self.status = gameStatusModel.GameStatus.EXITED


ttt = TicTacToe()
ttt.play()
