import random
import pygame

class MTile:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.tile_type = 0
        self.image = None
        self.rect = None

class MTable:
    def __init__(self, tiles):
        self.tiles = tiles
        self.start_x = 640
        self.start_y = 360
        self.selected = None

        random.shuffle(self.tiles)
        for index in range(0, len(self.tiles), 2):
            t = random.randint(1, 31)
            self.tiles[index].tile_type = t
            self.tiles[index+1].tile_type = t

        self.tiles.sort(key=lambda x: x.z)
        
        width = 0
        height = 0
        for tile in self.tiles:
            width = max(width, tile.x)
            height = max(height, tile.y)
            tile.image = pygame.image.load(f'assets/{tile.tile_type}.png')

        self.start_x -= width*44/2 + 22
        self.start_y -= height*60/2 + 30

        for tile in self.tiles:
            tile.rect = pygame.Rect(self.start_x + tile.x*44 + tile.z*2, self.start_y + tile.y*60 + tile.z*2, 44, 60)

    def draw_tiles(self, screen):
        for tile in self.tiles:
            screen.blit(tile.image, (tile.rect.x, tile.rect.y))
        
        if self.selected != None:
            s = pygame.Surface((44, 60))
            s.set_alpha(128)
            s.fill((0, 120, 200))
            screen.blit(s, (self.selected.rect.x, self.selected.rect.y))

    def check_tiles(self, event):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return
        
        for tile in self.tiles:
            if tile.rect.collidepoint(event.pos):
                if self.check_selection(tile) == False:
                    continue

                if self.selected != None:
                    self.check_move(tile)
                else:
                    self.selected = tile

    def check_selection(self, tile):
        left = False
        right = False

        for t in self.tiles:
            if t == tile:
                continue

            if abs(tile.x - t.x) < 1 and abs(tile.y - t.y) < 1 and tile.z < t.z:
                return False
            
            if t.x == tile.x-1 and abs(tile.y - t.y) < 1 and tile.z <= t.z:
                left = True
            
            if t.x == tile.x+1 and abs(tile.y - t.y) < 1 and tile.z <= t.z:
                right = True
        
        if left == True and right == True:
            return False
        return True

    def check_move(self, tile):
        if self.selected != tile and self.selected.tile_type == tile.tile_type:
            self.tiles.remove(self.selected)
            self.tiles.remove(tile)
        
        self.selected = None

