from TicTacToeNxN.exceptions.InvalidMoveException import InvalidMoveException
from TicTacToeNxN.models import account as accountModel
from TicTacToeNxN.models import piece as pieceModel
from TicTacToeNxN.models import pieceType as pieceTypeModel


class Player:
    account: accountModel.Account
    pieceIdentifier: pieceTypeModel.PieceType
    pieces: [pieceModel.Piece]

    def __init__(self, account: accountModel.Account, pieceIdentifier: pieceTypeModel.PieceType, pieces: [pieceModel.Piece]) -> None:
        self.account = account
        self.pieceIdentifier = pieceIdentifier
        self.pieces = pieces

    def removePiece(self, piece: pieceModel.Piece) -> None:
        try:
            self.pieces.remove(piece)
        except IndexError:
            raise InvalidMoveException
