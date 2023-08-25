import pygame
from player_answer import Player

pygame.init()
screen = pygame.display.set_mode((800, 600))

FPS = 60
clock = pygame.time.Clock()


def main():
    player = Player(screen=screen, speed=5)

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.update_speed_y(-1)
                if event.key == pygame.K_a:
                    player.update_speed_x(-1)
                if event.key == pygame.K_s:
                    player.update_speed_y(1)
                if event.key == pygame.K_d:
                    player.update_speed_x(1)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.update_speed_y(1)
                if event.key == pygame.K_a:
                    player.update_speed_x(1)
                if event.key == pygame.K_s:
                    player.update_speed_y(-1)
                if event.key == pygame.K_d:
                    player.update_speed_x(-1)

        player.update_position()
        screen.fill("cyan")
        player.render()
        pygame.display.update()


main()
