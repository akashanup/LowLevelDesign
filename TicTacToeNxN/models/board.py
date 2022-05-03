from typing import Optional, Union

from TicTacToeNxN.models.cell import Cell
from TicTacToeNxN.models.cellPosition import CellPosition
from TicTacToeNxN.models.piece import Piece
from TicTacToeNxN.models.pieceType import PieceType


class Board:
    size: int
    cells: [[Cell]]

    def __init__(self, size: int, cells: [[Cell]]) -> None:
        self.size = size
        self.cells = cells

    def getCell(self, position: CellPosition) -> Optional[Cell]:
        for cell in self.cells:
            if cell.cellPosition.r == position.r and cell.cellPosition.c == position.c:
                return cell
        return None

    @staticmethod
    def __checkWinner(pieces: [Union[Piece, PieceType]]) -> Optional[Piece]:
        winnerFound = True
        for i in range(1, len(pieces)):
            if (isinstance(pieces[i], PieceType) or isinstance(pieces[i-1], PieceType)) or (pieces[i].type.identifier() != pieces[i-1].type.identifier()):
                winnerFound = False
                break
        if winnerFound:
            return pieces[0].type.identifier()
        return None

    def __checkWinnerInRows(self) -> Optional[Piece]:
        # Checking rows
        for r in range(self.size):
            pieces = []
            for cell in self.cells:
                if cell.cellPosition.r == r:
                    pieces.append(cell.piece)
            winner = Board.__checkWinner(pieces)
            if winner:
                return winner
        return None

    def __checkWinnerInColumns(self) -> Optional[Piece]:
        # Checking columns
        for c in range(self.size):
            pieces = []
            for cell in self.cells:
                if cell.cellPosition.c == c:
                    pieces.append(cell.piece)
            winner = Board.__checkWinner(pieces)
            if winner:
                return winner
        return None

    def __checkWinnerInDiagonals(self) -> Optional[Piece]:
        # Checking forward diagonal
        r, c = 0, 0
        pieces = []
        while r < self.size and c < self.size:
            for cell in self.cells:
                if cell.cellPosition.c == c and cell.cellPosition.r == r:
                    pieces.append(cell.piece)
            r += 1
            c += 1
        winner = Board.__checkWinner(pieces)
        if winner:
            return winner

        # Checking backward diagonal
        r, c = 0, self.size-1
        pieces = []
        while r < self.size and c >= 0:
            for cell in self.cells:
                if cell.cellPosition.c == c and cell.cellPosition.r == r:
                    pieces.append(cell.piece)
            r += 1
            c -= 1
        winner = Board.__checkWinner(pieces)
        if winner:
            return winner

        return None

    def checkForWinner(self) -> Optional[Piece]:
        winner = self.__checkWinnerInRows()
        if not winner:
            winner = self.__checkWinnerInColumns()
            if not winner:
                winner = self.__checkWinnerInDiagonals()
        return winner

    def printCurrentState(self) -> None:
        currentRow = self.cells[0].cellPosition.r
        for cell in self.cells:
            row = cell.cellPosition.r
            if row != currentRow:
                currentRow = row
                print()
            piece = cell.piece
            if not isinstance(piece, PieceType):
                print(piece.type.identifier().value, end=' ')
            else:
                print(PieceType.getIdentifier().value, end=' ')
        print()

    def checkForGameOver(self) -> bool:
        for cell in self.cells:
            if cell.isEmpty():
                return False
        return True
