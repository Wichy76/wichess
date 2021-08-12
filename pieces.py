NONE = (-1, -1)
KING = 1
PAWN = 2
KNIGHT = 3
BISHOP = 4
ROOK = 5
QUEEN = 6

WHITE = 0
BLACK = 1

images = {
    (0, 1): 'pieces/WhiteKing.png',
    (0, 2): 'pieces/WhitePawn.png',
    (0, 3): 'pieces/WhiteKnight.png',
    (0, 4): 'pieces/WhiteBishop.png',
    (0, 5): 'pieces/WhiteRook.png',
    (0, 6): 'pieces/WhiteQueen.png',
    (1, 1): 'pieces/BlackKing.png',
    (1, 2): 'pieces/BlackPawn.png',
    (1, 3): 'pieces/BlackKnight.png',
    (1, 4): 'pieces/BlackBishop.png',
    (1, 5): 'pieces/BlackRook.png',
    (1, 6): 'pieces/BlackQueen.png'
}

fen_dict = {
    'K': (0, 1),
    'P': (0, 2),
    'N': (0, 3),
    'B': (0, 4),
    'R': (0, 5),
    'Q': (0, 6),
    'k': (1, 1),
    'p': (1, 2),
    'n': (1, 3),
    'b': (1, 4),
    'r': (1, 5),
    'q': (1, 6)
}