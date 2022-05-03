from TicTacToeNxN.exceptions.InvalidMoveException import InvalidMoveException
from TicTacToeNxN.models import board as boardModel
from TicTacToeNxN.models import cellPosition as cellPositionModel
from TicTacToeNxN.models import piece as pieceModel
from TicTacToeNxN.models import player as playerModel


class Move:
    player: playerModel.Player
    piece: pieceModel.Piece
    position: cellPositionModel.CellPosition

    def __init__(self, player: playerModel.Player, piece: pieceModel.Piece, position: cellPositionModel.CellPosition):
        self.player = player
        self.piece = piece
        self.position = position

    def validate(self, board: boardModel.Board) -> bool:
        if not self.player.pieces:
            raise InvalidMoveException
        cell = board.getCell(self.position)
        if not cell:
            raise InvalidMoveException
        return cell.isEmpty()

    def make(self, board: boardModel.Board) -> None:
        cell = board.getCell(self.position)
        cell.updatePiece(self.piece)
        self.player.removePiece(self.piece)


