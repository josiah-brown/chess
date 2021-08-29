import pygame
from piece import Piece


class Board:
    """Class that represents the current status of each square on the board"""
    def __init__(self, position_list):
        self.img = pygame.image.load("assets/board.png")
        self.squares = position_list

    def set_board(self, positions: list):
        """Pass in a list of 64 positions and the board squares will update"""
        self.squares = []
        for p in positions:
            self.squares.append(p)

    def get_position_from_click(self, click) -> tuple:
        r, c = 0, 0

        if click[0] < 100:
            c = 1
        elif click[0] < 200:
            c = 2
        elif click[0] < 300:
            c = 3
        elif click[0] < 400:
            c = 4
        elif click[0] < 500:
            c = 5
        elif click[0] < 600:
            c = 6
        elif click[0] < 700:
            c = 7
        elif click[0] < 800:
            c = 8

        if click[1] < 100:
            r = 8
        elif click[1] < 200:
            r = 7
        elif click[1] < 300:
            r = 6
        elif click[1] < 400:
            r = 5
        elif click[1] < 500:
            r = 4
        elif click[1] < 600:
            r = 3
        elif click[1] < 700:
            r = 2
        elif click[1] < 800:
            r = 1
        return r, c

    def select_clicked_piece(self, click: tuple):
        """Pass in a click tuple and select the piece in squares that was clicked"""
        position = self.get_position_from_click(click)
        r = position[0]
        c = position[1]

        for s in self.squares:
            if s:
                if s.row == r and s.col == c:
                    print(f"Piece on row {r} col {c} selected")
                    if s.selected:
                        s.selected = False
                    else:
                        s.selected = True
                else:
                    s.selected = False

    def clicked_a_piece(self, click: tuple) -> bool:
        position = self.get_position_from_click(click)
        r = position[0]
        c = position[1]

        for s in self.squares:
            if s:
                if s.row == r and s.col == c:
                    return True
        return False

    def get_clicked_piece(self, click: tuple) -> Piece:
        """Pass in a click tuple and select the piece in squares that was clicked"""
        position = self.get_position_from_click(click)
        r = position[0]
        c = position[1]

        for s in self.squares:
            if s:
                if s.row == r and s.col == c:
                    return s

    def deselect_all(self):
        for s in self.squares:
            if s:
                s.selected = False;

    def clicked_possible_move(self, click: tuple):
        """Returns true if a click was made on a possible move of the selected piece"""
        position = self.get_position_from_click(click)
        r = position[0]
        c = position[1]
        for s in self.squares:
            if s and s.selected:
                for move in s.possible_moves:
                    if move[0] == r and move[1] == c:
                        return True

    def move_selected_piece(self, click):
        position = self.get_position_from_click(click)
        r = position[0]
        c = position[1]
        for p in self.squares:
            if p:
                if p.selected:
                    p.row = r
                    p.col = c
                    p.selected = False
                    p.possible_moves = []