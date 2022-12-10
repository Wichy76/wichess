import Pieces
import itertools
import ChessBoard
from rules import Pawn


def set_movement_info(selected_piece, new_pos, last_move, board,  n):
    ChessBoard.piece, ChessBoard.old_x, ChessBoard.old_y = selected_piece[0], selected_piece[1] // n, selected_piece[
        2] // n
    ChessBoard.new_x, ChessBoard.new_y = new_pos[0] // n, new_pos[1] // n
    ChessBoard.last_x, ChessBoard.last_y = last_move[1] // n, last_move[2] // n
    ChessBoard.last_piece = last_move[0]
    ChessBoard.board = board

    return None
def is_valid_move(selected_piece, new_pos, current_turn, board, last_move, n):
    piece, old_x, old_y = selected_piece
    new_x, new_y = new_pos

    set_movement_info(selected_piece, new_pos, last_move, board, n)
    if old_x // n == new_x // n and old_y // n == new_y // n:
        return False
    elif board[new_x // n][new_y // n][0] == current_turn:
        return False
    elif piece == (current_turn, Pieces.PAWN):
        return Pawn.valid_movement(current_turn)
    elif piece == (current_turn, Pieces.KNIGHT):
        return valid_knight_movement(selected_piece, new_pos, current_turn, n)
    elif piece == (current_turn, Pieces.KING):
        return valid_king_movement(selected_piece, new_pos, current_turn, n)
    elif piece == (current_turn, Pieces.ROOK):
        return valid_rook_movement(selected_piece, new_pos, current_turn, board, n)
    elif piece == (current_turn, Pieces.BISHOP):
        return valid_bishop_movement(selected_piece, new_pos, current_turn, board, n)
    elif piece == (current_turn, Pieces.QUEEN):
        return valid_queen_movement(selected_piece, new_pos, current_turn, board, n)
    else:
        return False


def valid_knight_movement(selected_piece, new_pos, current_turn, n):
    possibles = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
    piece, old_x, old_y = selected_piece[0], selected_piece[1] // n, selected_piece[2] // n
    new_x, new_y = new_pos[0] // n, new_pos[1] // n
    if piece != (current_turn, Pieces.KNIGHT):
        return False
    else:
        for posi in possibles:
            if old_x == new_x + int(posi[0]) and old_y == new_y + int(posi[1]):
                return True

    return False


def valid_king_movement(selected_piece, new_pos, current_turn, n):
    possibles = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
    piece, old_x, old_y = selected_piece[0], selected_piece[1] // n, selected_piece[2] // n
    new_x, new_y = new_pos[0] // n, new_pos[1] // n
    if piece != (current_turn, Pieces.KING):
        return False
    else:
        for posi in possibles:
            if old_x == new_x + int(posi[0]) and old_y == new_y + int(posi[1]):
                return True

    return False


def is_horizontal_or_vertical_move(new_x, new_y, old_x, old_y):
    if old_x == new_x and old_y != new_y or old_x != (
            new_x) and old_y == new_y:
        return True


def valid_rook_movement(selected_piece, new_pos, current_turn, board, n):
    piece, old_x, old_y = selected_piece[0], selected_piece[1] // n, selected_piece[2] // n
    new_x, new_y = new_pos[0] // n, new_pos[1] // n
    if piece != (current_turn, Pieces.ROOK):
        return False
    else:
        if is_horizontal_or_vertical_move(new_x, new_y, old_x, old_y):
            if have_between_own_pieces_horizontal(new_pos, board, selected_piece, n) or have_between_own_pieces_vertical(
                    new_pos, board, selected_piece, n):
                return False
            return True

    return False


def is_diagonal_move(new_x, new_y, old_x, old_y):
    if old_x - old_y == new_x - new_y or old_x + (
            old_y) == new_x + new_y:
        return True


def valid_bishop_movement(selected_piece, new_pos, current_turn, board, n):
    piece, old_x, old_y = selected_piece[0], selected_piece[1] // n, selected_piece[2] // n
    new_x, new_y = new_pos[0] // n, new_pos[1] // n
    if piece != (current_turn, Pieces.BISHOP):
        return False
    else:
        if is_diagonal_move(new_x, new_y, old_x, old_y):
            if have_between_own_pieces_diagonal(new_pos, board, selected_piece, n):
                return False
            return True

    return False


def valid_queen_movement(selected_piece, new_pos, current_turn, board, n):
    piece, old_x, old_y = selected_piece[0], selected_piece[1] // n, selected_piece[2] // n
    new_x, new_y = new_pos[0] // n, new_pos[1] // n
    if piece != (current_turn, Pieces.QUEEN):
        return False
    else:
        if is_diagonal_move(new_x, new_y, old_x, old_y):
            if have_between_own_pieces_diagonal(new_pos, board, selected_piece, n):
                return False
            return True
        if is_horizontal_or_vertical_move(new_x, new_y, old_x, old_y):
            if have_between_own_pieces_horizontal(new_pos, board, selected_piece, n) or have_between_own_pieces_vertical(
                    new_pos, board, selected_piece, n):
                return False
            return True

    return False


def have_between_own_pieces_vertical(new_pos, board, selected_piece, n):
    piece, old_x, old_y = selected_piece[0], selected_piece[1] // n, selected_piece[2] // n
    new_x, new_y = new_pos[0] // n, new_pos[1] // n
    min_y = min(new_y, old_y) + 1
    max_y = max(new_y, old_y)
    for y in range(min_y, max_y):
        if board[old_x][y][0] == piece[0]:
            return True
    return False


def have_between_own_pieces_horizontal(new_pos, board, selected_piece, n):
    piece, old_x, old_y = selected_piece[0], selected_piece[1] // n, selected_piece[2] // n
    new_x, new_y = new_pos[0] // n, new_pos[1] // n
    min_x = min(new_x, old_x) + 1
    max_x = max(new_x, old_x)
    for x in range(min_x, max_x):
        if board[x][old_y][0] == piece[0]:
            return True
    return False


def have_between_own_pieces_diagonal(new_pos, board, selected_piece, n):
    piece, old_x, old_y = selected_piece[0], selected_piece[1] // n, selected_piece[2] // n
    new_x, new_y = new_pos[0] // n, new_pos[1] // n
    min_x = min(new_x, old_x) + 1
    max_x = max(new_x, old_x)

    if new_y + new_x == old_y + old_x:
        for x in range(min_x, max_x):
            y = (old_y + old_x) - x
            if board[x][y][0] == piece[0]:
                return True
    else:
        for x in range(min_x, max_x):
            y = (old_y - old_x) + x
            if board[x][y][0] == piece[0]:
                return True
    return False
