from TicTacToeNxN.interfaces.iPiece import IPiece
from TicTacToeNxN.models.pieceType import PieceType


class RoundPiece(IPiece):
    pieceType: PieceType

    def __init__(self):
        self.pieceType = PieceType.ROUND

    def identifier(self) -> PieceType:
        return self.pieceType
