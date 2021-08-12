import pygame
import pieces

def create_board():
    board = []
    for y in range(8):
        board.append([])
        for x in range(8):
            board[y].append(pieces.NONE)
    board[-4][-5] = (pieces.WHITE, pieces.QUEEN)
    return board

def drawSquare(gameDisplay, x, y, color, pieceImg):
    pygame.draw.rect(gameDisplay, color, (x, y, 100, 100))
    if pieceImg != pieces.NONE:
        gameDisplay.blit(pieceImg, (x + 10, y + 10))

def getImage(piece):
    if piece == pieces.NONE:
        return piece
    return pygame.image.load(pieces.images[piece])

def main():
    pygame.init()

    display_width = 800
    display_height = 800

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Wichess')

    black = (100, 100, 100)
    white = (180, 180, 180)
    clock = pygame.time.Clock()

    board = create_board()
    end = False

    while not end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        gameDisplay.fill(white)

        for x in range(0, 8):
            for y in range(0, 8):
                drawSquare(gameDisplay,
                           x * 100,
                           y * 100,
                           white if (x + y) % 2 == 0 else black,
                           getImage(board[x][y]))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
