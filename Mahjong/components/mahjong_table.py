import random

class MTile:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.tile_type = 0

class MTable:
    def __init__(self, tiles):
        self.tiles = tiles