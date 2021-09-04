import pygame
from custom_functions import *
import copy


class Board:
    """Class that represents the current status of each square on the board"""
    def __init__(self, position_list):
        self.img = pygame.image.load("assets/board.png")
        self.squares = position_list

    def set_board(self, positions: list):
        """Pass in a 2d list of positions and the board squares will update (useful later for setting up end games)"""
        self.squares = []
        for p in positions:
            self.squares.append(p)

    def get_clicked_piece(self, click: tuple):
        """Returns piece that was clicked or None if square is empty"""
        r_click, c_click = get_row_col_from_click(click)

        for s in self.squares:
            if s:
                if s.row == r_click and s.col == c_click:
                    return s
        return None

    def deselect_all(self):
        """Deselects all of the squares"""
        for s in self.squares:
            if s:
                s.selected = False

    def kill_piece(self, index):
        self.squares[index] = None

    def move_piece(self, old_pos_index, new_r_c):
        """Moves the selected piece to clicked square, clears possible moves, and deselects"""
        r_new, c_new = new_r_c
        new_index = get_index_from_row_col((r_new, c_new))

        # Remove opposing piece if attack was made
        if self.squares[new_index]:
            self.kill_piece(new_index)
        # New square contains the piece
        self.squares[new_index] = self.squares[old_pos_index]
        # Update piece index
        self.squares[new_index].board_index = new_index
        # Clear possible moves
        self.squares[new_index].possible_moves = []
        # Remove piece from old square
        self.squares[old_pos_index] = None

    def checkmate(self, color):
        """Given a color, returns True if that color is mated"""
        for piece in self.squares:
            if piece and piece.color == color:
                piece.calculate_moves(self)
                for move in piece.possible_moves:
                    past_index = piece.board_index
                    proposed_move_index = get_index_from_row_col(move)
                    future_board = Board(copy.copy(self.squares))
                    future_board.squares[proposed_move_index] = copy.copy(piece)
                    future_board.squares[proposed_move_index].board_index = proposed_move_index
                    future_board.squares[past_index] = None
                    if not king_is_in_check(future_board, color):
                        return False
                    del future_board
        return True
