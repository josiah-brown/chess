import pygame

class Piece:
    """Class that represents a generic chess piece"""
    def __init__(self, img_path, row, col):
        self.img = pygame.image.load(img_path)
        self.rect = self.img.get_rect()
        self.row = row
        self.col = col

    def display_piece(self):
        self.img.blit()
