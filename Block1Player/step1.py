import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

"""
this is basic pygame code.

The code update the screen every frame, but it doesn't draw anything on the screen.
"""
