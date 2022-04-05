class Board:

    PIECES = {
        'white': {
            'king': '♔',
            'queen': '♕',
            'bishop': '♗',
            'knight': '♘',
            'rook': '♖',
            'pawn': '♙' 
        },
        'black': {
            'king': '♚',
            'queen': '♛',
            'bishop': '♝',
            'knight': '♞',
            'rook': '♜',
            'pawn': '♟'
        }
    }

    def __init__(self):
        self.board = [
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        ]

    def show(self):
        # Return the board to display in grid form
        for row in self.board:
            print(' | '.join(row))
            print('--|---|---|---|---|---|---|---')

b = Board()
print(b.PIECES['black']['queen'])