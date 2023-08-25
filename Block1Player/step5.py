import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

player_width = 50
player_height = 50

player_pos_x = 0
player_pos_y = 0

player_speed_x = 0
player_speed_y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_speed_y = -0.5
                player_speed_x = 0
            if event.key == pygame.K_a:
                player_speed_y = 0
                player_speed_x = -0.5
            if event.key == pygame.K_s:
                player_speed_y = 0.5
                player_speed_x = 0
            if event.key == pygame.K_d:
                player_speed_y = 0
                player_speed_x = 0.5

    player_pos_x += player_speed_x
    player_pos_y += player_speed_y

    screen.fill("cyan")
    pygame.draw.rect(screen, "red", (player_pos_x,
                     player_pos_y, player_width, player_height))
    pygame.display.update()

"""
Add player speed_x and speed_y variables.
update player position by adding speed_x and speed_y to player_pos_x and player_pos_y.

but player not stop when the key is released.
"""
