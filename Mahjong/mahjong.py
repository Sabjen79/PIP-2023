import pygame
from components.level_loader import LevelLoader

success, fails = pygame.init()
print(f"{success} successes and {fails} failures")

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
FPS = 60 

level_loader = LevelLoader(screen)

while True:
    clock.tick(60)
    screen.fill((255, 255, 255))

    level = level_loader.active_level
    if level == None:
        level_loader.draw_buttons()
    else:
        level.draw_tiles(screen)

    for event in pygame.event.get():
        if level == None:
            level_loader.check_buttons(event)
        else:
            level.check_tiles(event)

        if event.type == pygame.QUIT:
            quit()
    
    if level != None and len(level.tiles) == 0:
        level_loader.active_level = None

    pygame.display.update()