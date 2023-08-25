import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

player_width = 50
player_height = 50

player_pos_x = 0
player_pos_y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_pos_y -= 5
            if event.key == pygame.K_a:
                player_pos_x -= 5
            if event.key == pygame.K_s:
                player_pos_y += 5
            if event.key == pygame.K_d:
                player_pos_x += 5

    screen.fill("cyan")
    pygame.draw.rect(screen, "red", (player_pos_x,
                     player_pos_y, player_width, player_height))
    pygame.display.update()

"""
fill the screen with cyan color.

but we can't hold the key to move the player.
"""
