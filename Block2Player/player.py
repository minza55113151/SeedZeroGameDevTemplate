import pygame


class Player:
    def __init__(self, width=50, height=50, pos_x=0, pos_y=0, speed=0.5,
                 screen=None):
        player_image = pygame.image.load("block.png")
        player_image = pygame.transform.scale(player_image, (width, height))
        self.image = player_image
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.speed_x = 0
        self.speed_y = 0
        self.screen = screen

    def update_speed_x(self, direction):
        self.speed_x += direction * self.speed

    def update_speed_y(self, direction):
        self.speed_y += direction * self.speed

    def update_position(self):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        self.__manage_player_out_of_bound()

    def __manage_player_out_of_bound(self):
        if self.pos_x < 0:
            self.pos_x += self.screen.get_width()
        if self.pos_x > self.screen.get_width():
            self.pos_x -= self.screen.get_width()
        if self.pos_y < 0:
            self.pos_y += self.screen.get_height()
        if self.pos_y > self.screen.get_height():
            self.pos_y -= self.screen.get_height()

    def render(self):
        self.screen.blit(self.image, (self.pos_x, self.pos_y))
