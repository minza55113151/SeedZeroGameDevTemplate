import pygame
from player import Player

pygame.init()
screen = pygame.display.set_mode((800, 600))

FPS = 60
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 20, True)


def main():
    is_running = True
    player = Player(screen=screen, speed=5)

    time_left = 10

    while is_running:
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

        text = font.render(f"Time left: {time_left:.2f}", True, "black")
        text_rect = text.get_rect()

        if time_left <= 0:
            text = font.render("Time out", True, "black")
            is_running = False

        screen.fill("cyan")
        player.render()
        screen.blit(text, (screen.get_width() / 2 - text_rect.width / 2,
                           screen.get_height() / 2 - text_rect.height / 2))
        pygame.display.update()


main()
