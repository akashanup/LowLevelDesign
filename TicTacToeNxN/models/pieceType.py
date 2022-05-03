from enum import Enum
from typing import Optional


class PieceType(Enum):
    CROSS = 'X'
    ROUND = 'O'
    BLANK = '-'

    @staticmethod
    def getIdentifier(identifier: Optional[str] = None):
        if identifier == PieceType.CROSS.value:
            return PieceType.CROSS
        elif identifier == PieceType.ROUND.value:
            return PieceType.ROUND
        else:
            return PieceType.BLANK
