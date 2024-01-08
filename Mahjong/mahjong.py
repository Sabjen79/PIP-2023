import pygame
from components.level_loader import LevelLoader

success, fails = pygame.init()
print(f"{success} successes and {fails} failures")

screen = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
FPS = 60 

level_loader = LevelLoader(screen)

while True:
    clock.tick(60)
    screen.fill((255, 255, 255))

    if level_loader.active_level == None:
        level_loader.draw_buttons()

    for event in pygame.event.get():
        if level_loader.active_level == None:
            level_loader.check_buttons(event)
            
        if event.type == pygame.QUIT:
            quit()
    
    pygame.display.update()