from TicTacToeNxN.interfaces.iPiece import IPiece
from TicTacToeNxN.models.pieceType import PieceType


class CrossPiece(IPiece):
    pieceType: PieceType

    def __init__(self):
        self.pieceType = PieceType.CROSS

    def identifier(self) -> PieceType:
        return self.pieceType
