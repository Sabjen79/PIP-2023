import os
import pygame
from components.mahjong_table import MTile, MTable

class LevelLoader:
    def __init__(self, screen):
        self.buttons = []
        self.screen = screen
        self.active_level = None

        for index, file in enumerate(os.listdir("./levels")):
            self.buttons.append(Button(310, 50+index*50, file))

    def draw_buttons(self):
        for button in self.buttons:
            button.draw(self.screen)

    def check_buttons(self, event):
        for button in self.buttons:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):
                    self.active_level = self.load_level(button.file)

    def load_level(self, file):
        tiles = []

        with open("./levels/" + file) as f:
            for line in f.readlines():
                args = [float(x) for x in line.strip()[2:].split(' ')]
                
                match line[0]:
                    case 'p':
                        tiles.append(MTile(args[0], args[1], args[2]))
                    case 'r':
                        for num in range(int(args[3])):
                            tiles.append(MTile(args[0] + num, args[1], args[2]))
                    case 'c':
                        for num in range(int(args[3])):
                            tiles.append(MTile(args[0], args[1] + num, args[2]))
            
        return MTable(tiles)


class Button:
    def __init__(self, x, y, file):
        self.rect = pygame.Rect(x, y, 100, 40)
        self.file = file

    def draw(self, surface):
        pygame.draw.rect(surface, (200, 200, 200), self.rect)
        font = pygame.font.Font(None, 24)
        text = font.render(self.file, True, (0,0,0))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

        