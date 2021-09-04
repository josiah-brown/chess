import pygame
from custom_functions import *


class Piece:
    """Class that represents a generic chess piece"""
    def __init__(self, img_path, row, col, piece_type, color):
        self.img = pygame.image.load(img_path)
        self.rect = self.img.get_rect()
        self.board_index = (col - 1) + (row - 1) * 8
        self.selected = False
        self.piece_type = piece_type
        self.color = color
        self.possible_moves = []
        self.moved = False

    def calculate_moves(self, b):
        """Pass in the current board and set the pieces possible_moves attribute to a list of all possible moves"""
        available_moves = []
        row, col = get_row_col_from_index(self.board_index)

        if self.piece_type == "p":
            if self.color == "w":
                if row == 2:
                    if square_is_empty(b, (3, col)):
                        available_moves.append((3, col))
                        if square_is_empty(b, (4, col)):
                            available_moves.append((4, col))
                elif row < 8:
                    if square_is_empty(b, (row + 1, col)):
                        available_moves.append((row + 1, col))
                attacks = [(row + 1, col - 1), (row + 1, col + 1)]
                for move in attacks:
                    if move[0] < 1 or move[0] > 8 or move[1] > 8 or move[1] < 1:
                        continue
                    else:
                        if is_enemy(b, move, self.color):
                            available_moves.append(move)
            if self.color == "b":
                if row == 7:
                    if square_is_empty(b, (6, col)):
                        available_moves.append((6, col))
                        if square_is_empty(b, (5, col)):
                            available_moves.append((5, col))
                elif row > 1:
                    if square_is_empty(b, (row - 1, col)):
                        available_moves.append((row - 1, col))
                attacks = [(row - 1, col - 1), (row - 1, col + 1)]
                for move in attacks:
                    if move[0] < 1 or move[0] > 8 or move[1] > 8 or move[1] < 1:
                        continue
                    else:
                        if is_enemy(b, move, self.color):
                            available_moves.append(move)

        if self.piece_type == "b":
            for i, c in enumerate(range(col, 8)):
                if square_is_empty(b, (row + i + 1, c + 1)):
                    available_moves.append((row + i + 1, c + 1))
                elif is_enemy(b, (row + i + 1, c + 1), self.color):
                    available_moves.append((row + i + 1, c + 1))
                    break
                else:
                    break
            for i, c in enumerate(range(col, 8)):
                if square_is_empty(b, (row - (i + 1), c + 1)):
                    available_moves.append((row - (i + 1), c + 1))
                elif is_enemy(b, (row - (i + 1), c + 1), self.color):
                    available_moves.append((row - (i + 1), c + 1))
                    break
                else:
                    break
            for i, c in reversed(list(enumerate(range(1, col)))):
                if square_is_empty(b, (row - (col - (i + 1)), c)):
                    available_moves.append((row - (col - (i + 1)), c))
                elif is_enemy(b, (row - (col - (i + 1)), c), self.color):
                    available_moves.append((row - (col - (i + 1)), c))
                    break
                else:
                    break
            for i, c in reversed(list(enumerate(range(1, col)))):
                if square_is_empty(b, (row + (col - (i + 1)), c)):
                    available_moves.append((row + (col - (i + 1)), c))
                elif is_enemy(b, (row + (col - (i + 1)), c), self.color):
                    available_moves.append((row + (col - (i + 1)), c))
                    break
                else:
                    break

        if self.piece_type == "r":
            for i in range(col+1, 9):
                if square_is_empty(b, (row, i)):
                    available_moves.append((row, i))
                elif is_enemy(b, (row, i), self.color):
                    available_moves.append((row, i))
                    break
                else:
                    break
            for i in reversed(range(1, col)):
                if square_is_empty(b, (row, i)):
                    available_moves.append((row, i))
                elif is_enemy(b, (row, i), self.color):
                    available_moves.append((row, i))
                    break
                else:
                    break
            for i in range(row+1, 9):
                if square_is_empty(b, (i, col)):
                    available_moves.append((i, col))
                elif is_enemy(b, (i, col), self.color):
                    available_moves.append((i, col))
                    break
                else:
                    break
            for i in reversed(range(1, row)):
                if square_is_empty(b, (i, col)):
                    available_moves.append((i, col))
                elif is_enemy(b, (i, col), self.color):
                    available_moves.append((i, col))
                    break
                else:
                    break

        if self.piece_type == "q":
            for i, c in enumerate(range(col, 8)):
                if square_is_empty(b, (row + i + 1, c + 1)):
                    available_moves.append((row + i + 1, c + 1))
                elif is_enemy(b, (row + i + 1, c + 1), self.color):
                    available_moves.append((row + i + 1, c + 1))
                    break
                else:
                    break
            for i, c in enumerate(range(col, 8)):
                if square_is_empty(b, (row - (i + 1), c + 1)):
                    available_moves.append((row - (i + 1), c + 1))
                elif is_enemy(b, (row - (i + 1), c + 1), self.color):
                    available_moves.append((row - (i + 1), c + 1))
                    break
                else:
                    break
            for i, c in reversed(list(enumerate(range(1, col)))):
                if square_is_empty(b, (row - (col - (i + 1)), c)):
                    available_moves.append((row - (col - (i + 1)), c))
                elif is_enemy(b, (row - (col - (i + 1)), c), self.color):
                    available_moves.append((row - (col - (i + 1)), c))
                    break
                else:
                    break
            for i, c in reversed(list(enumerate(range(1, col)))):
                if square_is_empty(b, (row + (col - (i + 1)), c)):
                    available_moves.append((row + (col - (i + 1)), c))
                elif is_enemy(b, (row + (col - (i + 1)), c), self.color):
                    available_moves.append((row + (col - (i + 1)), c))
                    break
                else:
                    break
            for i in range(col + 1, 9):
                if square_is_empty(b, (row, i)):
                    available_moves.append((row, i))
                elif is_enemy(b, (row, i), self.color):
                    available_moves.append((row, i))
                    break
                else:
                    break
            for i in reversed(range(1, col)):
                if square_is_empty(b, (row, i)):
                    available_moves.append((row, i))
                elif is_enemy(b, (row, i), self.color):
                    available_moves.append((row, i))
                    break
                else:
                    break
            for i in range(row + 1, 9):
                if square_is_empty(b, (i, col)):
                    available_moves.append((i, col))
                elif is_enemy(b, (i, col), self.color):
                    available_moves.append((i, col))
                    break
                else:
                    break
            for i in reversed(range(1, row)):
                if square_is_empty(b, (i, col)):
                    available_moves.append((i, col))
                elif is_enemy(b, (i, col), self.color):
                    available_moves.append((i, col))
                    break
                else:
                    break

        if self.piece_type == "k":
            for y in range(row-1, row+2):
                for x in range(col-1, col+2):
                    if square_is_empty(b, (y, x)) or is_enemy(b, (y, x), self.color):
                        available_moves.append((y, x))

        if self.piece_type == "n":
            n_moves = [(row + 2, col - 1), (row + 2, col + 1),
                       (row + 1, col + 2), (row - 1, col + 2),
                       (row - 2, col + 1), (row - 2, col - 1),
                       (row - 1, col - 2), (row + 1, col - 2)]
            for move in n_moves:
                if square_is_empty(b, move) or is_enemy(b, move, self.color):
                    available_moves.append(move)

        # Remove all moves that fall off the board
        for i, move in reversed(list(enumerate(available_moves))):
            # print(i, move)
            if move[0] < 1 or move[0] > 8 or move[1] > 8 or move[1] < 1:
                available_moves.pop(i)

        # Remove all moves that land on another piece of same color
        for s in b.squares:
            if s:
                pos = get_row_col_from_index(s.board_index)
                if pos in available_moves:
                    if s.color == self.color:
                        available_moves.remove((s.row, s.col))

        self.possible_moves = available_moves

    def clicked_possible_move(self, click: tuple):
        """Returns true if a click was made on a possible move of the selected piece"""
        pos = get_row_col_from_click(click)

        for move in self.possible_moves:
            if pos == move:
                return True
        return False
