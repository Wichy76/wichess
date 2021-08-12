import pieces
import itertools


def valid_pawn_movement(selected_piece, new_pos, current_turn):
    piece, old_x, old_y = selected_piece
    new_x, new_y = new_pos
    if piece != (current_turn, pieces.PAWN):
        return False
    else:
        if current_turn == pieces.WHITE:
            if old_x // 100 == new_x // 100 and old_y // 100 == (new_y // 100) + 1:
                return True
            elif old_x // 100 == new_x // 100 and old_y // 100 == 6 and (new_y // 100) == 4:
                return True
        if current_turn == pieces.BLACK:
            if old_x // 100 == new_x // 100 and old_y // 100 == (new_y // 100) - 1:
                return True
            elif old_x // 100 == new_x // 100 and old_y // 100 == 1 and (new_y // 100) == 3:
                return True

    return False


def valid_knight_movement(selected_piece, new_pos, current_turn):
    possibles = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
    piece, old_x, old_y = selected_piece
    new_x, new_y = new_pos
    if piece != (current_turn, pieces.KNIGHT):
        return False
    else:
        for posi in possibles:
            if old_x // 100 == (new_x // 100) + int(posi[0]) and old_y // 100 == (new_y // 100) + int(posi[1]):
                return True

    return False


def valid_king_movement(selected_piece, new_pos, current_turn):
    possibles = list(itertools.product([-1, 0, 1], [-1, 0, 1]))
    piece, old_x, old_y = selected_piece
    new_x, new_y = new_pos
    if piece != (current_turn, pieces.KING):
        return False
    else:
        for posi in possibles:
            if old_x // 100 == (new_x // 100) + int(posi[0]) and old_y // 100 == (new_y // 100) + int(posi[1]):
                return True

    return False


def is_horizontal_or_vertical_move(new_x, new_y, old_x, old_y):
    if old_x // 100 == (new_x // 100) and old_y // 100 != (new_y // 100) or old_x // 100 != (
            new_x // 100) and old_y // 100 == (new_y // 100):
        return True


def valid_rook_movement(selected_piece, new_pos, current_turn, board):
    piece, old_x, old_y = selected_piece
    new_x, new_y = new_pos
    if piece != (current_turn, pieces.ROOK):
        return False
    else:
        if is_horizontal_or_vertical_move(new_x, new_y, old_x, old_y):
            if have_between_own_pieces_horizontal(new_pos, board, selected_piece) or have_between_own_pieces_vertical(
                    new_pos, board, selected_piece):
                return False
            return True

    return False


def is_diagonal_move(new_x, new_y, old_x, old_y):
    if old_x // 100 - (old_y // 100) == new_x // 100 - (new_y // 100) or old_x // 100 + (
            old_y // 100) == new_x // 100 + (new_y // 100):
        return True


def valid_bishop_movement(selected_piece, new_pos, current_turn, board):
    piece, old_x, old_y = selected_piece
    new_x, new_y = new_pos
    if piece != (current_turn, pieces.BISHOP):
        return False
    else:
        if is_diagonal_move(new_x, new_y, old_x, old_y):
            if have_between_own_pieces_diagonal(new_pos, board, selected_piece) :
                return False
            return True

    return False


def valid_queen_movement(selected_piece, new_pos, current_turn, board):
    piece, old_x, old_y = selected_piece
    new_x, new_y = new_pos
    if piece != (current_turn, pieces.QUEEN):
        return False
    else:
        if is_diagonal_move(new_x, new_y, old_x, old_y):
            if have_between_own_pieces_diagonal(new_pos, board, selected_piece) :
                return False
            return True
        if is_horizontal_or_vertical_move(new_x, new_y, old_x, old_y):
            if have_between_own_pieces_horizontal(new_pos, board, selected_piece) or have_between_own_pieces_vertical(
                    new_pos, board, selected_piece):
                return False
            return True

    return False


def have_between_own_pieces_vertical(new_pos, board, selected_piece):
    piece, old_x, old_y = selected_piece
    new_x, new_y = new_pos
    min_y = min(new_y // 100, old_y // 100) + 1
    max_y = max(new_y // 100, old_y // 100)
    for y in range(min_y, max_y):
        if board[old_x // 100][y][0] == piece[0]:
            return True
    return False


def have_between_own_pieces_horizontal(new_pos, board, selected_piece):
    piece, old_x, old_y = selected_piece
    new_x, new_y = new_pos
    min_x = min(new_x // 100, old_x // 100) + 1
    max_x = max(new_x // 100, old_x // 100)
    for x in range(min_x, max_x):
        if board[x][old_y // 100][0] == piece[0]:
            return True
    return False


def have_between_own_pieces_diagonal(new_pos, board, selected_piece):
    piece, old_x, old_y = selected_piece
    new_x, new_y = new_pos
    min_x = min(new_x // 100, old_x // 100) + 1
    max_x = max(new_x // 100, old_x // 100)

    if new_y // 100 + new_x // 100 == old_y // 100 + old_x // 100:
        for x in range(min_x, max_x):
            y = (old_y // 100 + old_x // 100) - x
            if board[x][y][0] == piece[0]:
                return True
    else:
        for x in range(min_x, max_x):
            y = (old_y // 100 - old_x // 100) + x
            if board[x][y][0] == piece[0]:
                return True
    return False




