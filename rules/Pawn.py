import Pieces
import ChessBoard


def valid_movement(current_turn):
    if ChessBoard.piece != (current_turn, Pieces.PAWN):
        return False
    else:
        if current_turn == Pieces.WHITE:
            return valid_white_move()

        if current_turn == Pieces.BLACK:
            if ChessBoard.old_x == ChessBoard.new_x and ChessBoard.old_y == ChessBoard.new_y - 1:
                return True
            elif ChessBoard.old_x == ChessBoard.new_x and ChessBoard.old_y == 1 and ChessBoard.new_y == 3:
                return True
    return False


def valid_white_move():
    return white_pawn_move_1() or white_pawn_move_2() or white_en_passant()


def white_pawn_move_1():
    return ChessBoard.old_x == ChessBoard.new_x and ChessBoard.old_y == ChessBoard.new_y + 1


def white_pawn_move_2():
    return ChessBoard.old_x == ChessBoard.new_x and ChessBoard.old_y == 6 and ChessBoard.new_y == 4


def white_en_passant():
    if ChessBoard.last_piece == Pieces.PAWN and ChessBoard.last_x == ChessBoard.new_x \
            and ChessBoard.last_y == ChessBoard.new_y + 1 and ChessBoard.old_y == 3:
        ChessBoard.board[ChessBoard.last_x][ChessBoard.last_y] = Pieces.NONE
        return True
