from pieces.King import King
from pieces.Queen import Queen
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.Rook import Rook
from pieces.Pawn import Pawn

class ChessAPI:

    PIECES = {
        'King': {
            'abbr': 'k',
            'points': '#',
            'symbol': {
                'white': '♔',
                'black': '♚'
            }
        },
        'Queen': {
            'abbr': 'q',
            'points': '9',
            'symbol': {
                'white': '♕',
                'black': '♛'
            }
        },
        'Rook': {
            'abbr': 'r',
            'points': '5',
            'symbol': {
                'white': '♖',
                'black': '♜'
            }
        },
        'Bishop': {
            'abbr': 'b',
            'points': '3',
            'symbol': {
                'white': '♗',
                'black': '♝'
            }
        },
        'Knight': {
            'abbr': 'n',
            'points': '3',
            'symbol': {
                'white': '♘',
                'black': '♞'
            }
        },
        'Pawn': {
            'abbr': 'p',
            'points': '1',
            'symbol': {
                'white': '♙',
                'black': '♟'
            }
        },
    }
  
    def __init__(self):
        return 0

    def move (self):
        return 0

    def is_valid (self):
        return 0
