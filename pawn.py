from piece import Piece
import pygame


class Pawn(Piece):
    def __init__(self, color):
        self.color = color
        if color == 'w':
            self.img = pygame.image.load("assets/wp.png")
        else:
            self.img = pygame.image.load("assets/bp.png")