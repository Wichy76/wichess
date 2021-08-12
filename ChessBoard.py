import pygame
import pieces
import rules

black = (100, 100, 100)
white = (180, 180, 180)


def create_board():
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(pieces.NONE)

    return board


def draw_square(game_display, x, y, color, piece_img):
    pygame.draw.rect(game_display, color, (x, y, 100, 100))
    if piece_img != pieces.NONE:
        game_display.blit(piece_img, (x + 10, y + 10))


def draw_board(game_display, board):
    game_display.fill(white)

    for x in range(0, 8):
        for y in range(0, 8):
            draw_square(game_display,
                       x * 100,
                       y * 100,
                       white if (x + y) % 2 == 0 else black,
                       draw_image(board[x][y]))


def draw_image(piece):
    if piece == pieces.NONE:
        return piece
    return pygame.image.load(pieces.images[piece])


def get_square_under_mouse(board):
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    x, y = int(mouse_pos[0]), int(mouse_pos[1])
    return board[x // 100][y // 100], x, y


def draw_drag(game_display, board, selected_piece):
    if selected_piece:
        piece, x, y = get_square_under_mouse(board)
        if x is not None:
            pygame.draw.rect(game_display, (255, 0, 0), ((x // 100) * 100, (y // 100) * 100, 100, 100), 1)

        game_display.blit(draw_image(selected_piece[0]), (x - 40, y - 40))
        return x, y


def charge_fen(fen, board):
    fen_array = fen.split(' ')
    positions = fen_array[0].split('/')
    charge_fen_board(positions, board)
    current_turn = fen_current_turn(fen_array[1])
    return current_turn, None


def charge_fen_board(positions, board):
    for i, pos in enumerate(positions):
        j = 0
        for p in pos:
            if p.isnumeric():
                j += int(p)
            else:
                board[j][i] = pieces.fen_dict[p]
                j += 1


def fen_current_turn(turn):
    if turn == 'w':
        return pieces.WHITE
    else:
        return pieces.BLACK


def is_valid_move(selected_piece, new_pos, current_turn, board):
    piece, old_x, old_y = selected_piece
    new_x, new_y = new_pos
    if old_x // 100 == new_x // 100 and old_y // 100 == new_y // 100:
        return False
    if board[new_x // 100][new_y // 100][0] == current_turn:
        return False
    if piece == (current_turn, pieces.PAWN):
        return rules.valid_pawn_movement(selected_piece, new_pos, current_turn)
    if piece == (current_turn, pieces.KNIGHT):
        return rules.valid_knight_movement(selected_piece, new_pos, current_turn)
    if piece == (current_turn, pieces.KING):
        return rules.valid_king_movement(selected_piece, new_pos, current_turn)
    if piece == (current_turn, pieces.ROOK):
        return rules.valid_rook_movement(selected_piece, new_pos, current_turn, board)
    if piece == (current_turn, pieces.BISHOP):
        return rules.valid_bishop_movement(selected_piece, new_pos, current_turn, board)
    if piece == (current_turn, pieces.QUEEN):
        return rules.valid_queen_movement(selected_piece, new_pos, current_turn, board)
    else:
        return False


def main():
    pygame.init()

    display_width = 800
    display_height = 800

    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Wichess')
    clock = pygame.time.Clock()

    board = create_board()
    current_turn, juan = charge_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", board)
    end = False
    selected_piece = None
    drop_pos = None

    while not end:
        piece, x, y = get_square_under_mouse(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if piece != pieces.NONE:
                    selected_piece = piece, x, y
            if event.type == pygame.MOUSEBUTTONUP:
                if drop_pos and is_valid_move(selected_piece, drop_pos, current_turn, board):
                    piece, old_x, old_y = selected_piece
                    board[(old_x // 100)][(old_y // 100)] = pieces.NONE
                    new_x, new_y = drop_pos
                    board[(new_x // 100)][(new_y // 100)] = piece
                    current_turn = pieces.WHITE if current_turn != pieces.WHITE else pieces.BLACK
                selected_piece = None
                drop_pos = None
        draw_board(game_display, board)
        drop_pos = draw_drag(game_display, board, selected_piece)
        pygame.display.flip()


    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
