from abc import ABCMeta, abstractmethod

from TicTacToeNxN.models.pieceType import PieceType


class IPiece(metaclass=ABCMeta):
    pieceType: PieceType

    @abstractmethod
    def identifier(self) -> PieceType:
        """Abstract Method"""

