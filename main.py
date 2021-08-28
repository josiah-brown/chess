import sys
import pygame
from piece import Piece
from board import Board

white_pieces = [Piece("assets/wp.png", 2, 1),
                Piece("assets/wp.png", 2, 2),
                Piece("assets/wp.png", 2, 3),
                Piece("assets/wp.png", 2, 4),
                Piece("assets/wp.png", 2, 5),
                Piece("assets/wp.png", 2, 6),
                Piece("assets/wp.png", 2, 7),
                Piece("assets/wp.png", 2, 8),
                Piece("assets/wr.png", 1, 1),
                Piece("assets/wn.png", 1, 2),
                Piece("assets/wb.png", 1, 3),
                Piece("assets/wq.png", 1, 4),
                Piece("assets/wk.png", 1, 5),
                Piece("assets/wb.png", 1, 6),
                Piece("assets/wn.png", 1, 7),
                Piece("assets/wr.png", 1, 8)
                ]

black_pieces = [Piece("assets/bp.png", 7, 1),
                Piece("assets/bp.png", 7, 2),
                Piece("assets/bp.png", 7, 3),
                Piece("assets/bp.png", 7, 4),
                Piece("assets/bp.png", 7, 5),
                Piece("assets/bp.png", 7, 6),
                Piece("assets/bp.png", 7, 7),
                Piece("assets/bp.png", 7, 8),
                Piece("assets/br.png", 8, 1),
                Piece("assets/bn.png", 8, 2),
                Piece("assets/bb.png", 8, 3),
                Piece("assets/bq.png", 8, 4),
                Piece("assets/bk.png", 8, 5),
                Piece("assets/bb.png", 8, 6),
                Piece("assets/bn.png", 8, 7),
                Piece("assets/br.png", 8, 8)
                ]

# Initialize pygame
pygame.init()

# Create pygame screen
size = width, height = 800, 800
screen = pygame.display.set_mode(size)

# Initialize a game board
board = pygame.image.load("assets/board.png")

# Board = Board()
# for row in Board.squares:
#     for col in range(0, 8):
#         pass
#         # row.append()
# print(Board.squares)

# Begin the game
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill('#ffffff')
    screen.blit(board, (0, 0))
    for p in white_pieces:
        screen.blit(p.img, ((p.col - 1) * 100, height - p.row * 100))
    for p in black_pieces:
        screen.blit(p.img, ((p.col - 1) * 100, height - p.row * 100))
    pygame.display.flip()
