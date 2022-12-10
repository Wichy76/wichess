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
    (0, 1): 'Pieces/WhiteKing.png',
    (0, 2): 'Pieces/WhitePawn.png',
    (0, 3): 'Pieces/WhiteKnight.png',
    (0, 4): 'Pieces/WhiteBishop.png',
    (0, 5): 'Pieces/WhiteRook.png',
    (0, 6): 'Pieces/WhiteQueen.png',
    (1, 1): 'Pieces/BlackKing.png',
    (1, 2): 'Pieces/BlackPawn.png',
    (1, 3): 'Pieces/BlackKnight.png',
    (1, 4): 'Pieces/BlackBishop.png',
    (1, 5): 'Pieces/BlackRook.png',
    (1, 6): 'Pieces/BlackQueen.png'
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