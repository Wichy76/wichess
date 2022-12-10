import pygame
import Pieces
from rules import Rules

black = (100, 100, 100)
white = (180, 180, 180)

n = 75

global piece
global old_x
global old_y
global new_x
global new_y
global last_x
global last_y
global last_piece
global board
board = []



def create_board():
    global board
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(Pieces.NONE)

    return board


def draw_square(game_display, x, y, color, piece_img):
    pygame.draw.rect(game_display, color, (x, y, n, n))
    if piece_img != Pieces.NONE:
        game_display.blit(piece_img, (x - 2, y - 2))


def draw_board(game_display):
    game_display.fill(white)

    for x in range(0, 8):
        for y in range(0, 8):
            draw_square(game_display,
                        x * n,
                        y * n,
                        white if (x + y) % 2 == 0 else black,
                        draw_image(board[x][y]))


def draw_image(piece_1):
    if piece_1 == Pieces.NONE:
        return piece_1
    return pygame.image.load(Pieces.images[piece_1])


def get_square_under_mouse():
    mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
    x, y = int(mouse_pos[0]), int(mouse_pos[1])
    return board[x // n][y // n], x, y


def draw_drag(game_display, selected_piece):
    if selected_piece:
        piece, x, y = get_square_under_mouse()
        if x is not None:
            pygame.draw.rect(game_display, (255, 0, 0), ((x // n) * n, (y // n) * n, n, n), 1)

        game_display.blit(draw_image(selected_piece[0]), (x - 40, y - 40))
        return x, y


def charge_fen(fen):
    fen_array = fen.split(' ')
    positions = fen_array[0].split('/')
    charge_fen_board(positions)
    current_turn = fen_current_turn(fen_array[1])
    return current_turn, None


def charge_fen_board(positions):
    for i, pos in enumerate(positions):
        j = 0
        for p in pos:
            if p.isnumeric():
                j += int(p)
            else:
                board[j][i] = Pieces.fen_dict[p]
                j += 1


def fen_current_turn(turn):
    if turn == 'w':
        return Pieces.WHITE
    else:
        return Pieces.BLACK


def is_valid_move(selected_piece, new_pos, current_turn, last_move):
    return Rules.is_valid_move(selected_piece, new_pos, current_turn, board, last_move, n)


def main():
    pygame.init()

    display_width = 600
    display_height = 600

    game_display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Wichess')
    # clock = pygame.time.Clock()

    create_board()
    current_turn, juan = charge_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    end = False
    selected_piece = None
    drop_pos = None

    last_move = (Pieces.NONE, 0, 0)
    while not end:
        piece1, x, y = get_square_under_mouse()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if piece1 != Pieces.NONE:
                    selected_piece = piece1, x, y
            if event.type == pygame.MOUSEBUTTONUP:

                if drop_pos and is_valid_move(selected_piece, drop_pos, current_turn, last_move):
                    piece1, old_x_1, old_y_1 = selected_piece
                    board[(old_x_1 // n)][(old_y_1 // n)] = Pieces.NONE
                    new_x_1, new_y_1 = drop_pos
                    board[(new_x_1 // n)][(new_y_1 // n)] = piece1
                    current_turn = Pieces.WHITE if current_turn != Pieces.WHITE else Pieces.BLACK
                    last_move = (selected_piece[0][1], drop_pos[0], drop_pos[1])
                selected_piece = None
                drop_pos = None

        draw_board(game_display)
        drop_pos = draw_drag(game_display, selected_piece)
        pygame.display.flip()

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
