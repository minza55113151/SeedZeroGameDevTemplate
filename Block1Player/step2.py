import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

player_width = 50
player_height = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.draw.rect(screen, "red", (0, 0, player_width, player_height))
    pygame.display.update()


"""
Draw the player at the top left corner of the screen. with player_width and player_height as the width and height of the player.
color is "red".

but it standstill
"""
