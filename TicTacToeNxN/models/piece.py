from typing import Union

from TicTacToeNxN.models.crossPiece import CrossPiece
from TicTacToeNxN.models.roundPiece import RoundPiece


class Piece:
    type: Union[CrossPiece, RoundPiece]

    def __init__(self, pieceType: Union[CrossPiece, RoundPiece]):
        self.type = pieceType
