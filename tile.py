import pygame as pg

class Tile:
    def __init__(self, screen_width, column, speed):
        self.width = screen_width // 4
        self.height = 80
        self.column = column
        self.x = self.column * self.width
        self.y = -self.height
        self.speed = speed

    def move(self):
        self.y += self.speed

    def show(self, screen):
        pg.draw.rect(screen, (45, 45, 45), (self.x, self.y, self.width, self.height))
        pg.draw.rect(screen, (80, 80, 80), (self.x, self.y, self.width, 5))

    def get_hitbox(self):
        return pg.Rect(self.x + 5, self.y + 5, self.width - 10, self.height - 10)