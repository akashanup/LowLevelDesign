from typing import Union

from TicTacToeNxN.models.cellPosition import CellPosition
from TicTacToeNxN.models.piece import Piece
from TicTacToeNxN.models.pieceType import PieceType


class Cell:
    piece: Union[Piece, PieceType]
    cellPosition: CellPosition

    def __init__(self, piece: Union[Piece, PieceType], cellPosition: CellPosition) -> None:
        self.piece = piece
        self.cellPosition = cellPosition

    def isEmpty(self) -> bool:
        return self.piece == PieceType.BLANK

    def updatePiece(self, piece: Piece):
        self.piece = piece
