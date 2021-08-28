class Board:
    """Class that represents the current status of each square on the board"""
    def __init__(self):
        self.squares = [[] for _ in range(8)]