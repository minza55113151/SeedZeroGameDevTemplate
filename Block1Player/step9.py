import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

player_width = 50
player_height = 50

player_image = pygame.image.load("block.png")
player_image = pygame.transform.scale(
    player_image, (player_width, player_height))

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
                player_speed_y += -0.5
            if event.key == pygame.K_a:
                player_speed_x += -0.5
            if event.key == pygame.K_s:
                player_speed_y += 0.5
            if event.key == pygame.K_d:
                player_speed_x += 0.5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_speed_y += 0.5
            if event.key == pygame.K_a:
                player_speed_x += 0.5
            if event.key == pygame.K_s:
                player_speed_y += -0.5
            if event.key == pygame.K_d:
                player_speed_x += -0.5

    player_pos_x += player_speed_x
    player_pos_y += player_speed_y

    if player_pos_x < 0:
        player_pos_x += screen.get_width()
    if player_pos_x > screen.get_width():
        player_pos_x -= screen.get_width()
    if player_pos_y < 0:
        player_pos_y += screen.get_height()
    if player_pos_y > screen.get_height():
        player_pos_y -= screen.get_height()

    screen.fill("cyan")
    # pygame.draw.rect(screen, "red", (player_pos_x,
    #                  player_pos_y, player_width, player_height))
    screen.blit(player_image, (player_pos_x, player_pos_y))
    pygame.display.update()


"""
everything is ok now.

but out code is keep getting bigger and bigger.
"""
