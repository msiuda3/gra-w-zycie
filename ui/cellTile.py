import pygame

class cellTile:
    width = 20
    height = 20
    colorDead = (255, 0, 0)
    colorAlive = (0, 255, 0)
    def __init__(self, x, y, cell, surface):
        self.x = x
        self.y = y
        self.cell = cell
        self.surface = surface
    def draw(self):
        if self.cell.alive:
            cellColor = self.colorAlive
        else:
            cellColor = self.colorDead
        pygame.draw.rect(self.surface, cellColor, pygame.Rect(self.x, self.y, self.width, self.height))

    def onClick(self):
        self.cell.alive = not self.cell.alive
