from typing import Optional, Union
from TicTacToeNxN.models.crossPiece import CrossPiece
from TicTacToeNxN.models.piece import Piece
from TicTacToeNxN.models.roundPiece import RoundPiece
from TicTacToeNxN.models.pieceType import PieceType


class PieceFactory:

    @staticmethod
    def buildPiece(pieceIdentifier: Optional[str] = None) -> Union[Piece, PieceType]:
        if pieceIdentifier == PieceType.ROUND.value:
            return Piece(RoundPiece())
        elif pieceIdentifier == PieceType.CROSS.value:
            return Piece(CrossPiece())
        else:
            return PieceType.BLANK
