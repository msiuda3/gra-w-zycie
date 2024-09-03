import pygame

class NextCycleButton:
    def __init__(self, x, y, simulation):
        self.x = x
        self.y = y
        self.surface = pygame.display.set_mode((800,600))
        self.width = 430
        self.height = 30
        self.color = (25, 25, 25)
        self.simulation = simulation

        textColor = (222, 222, 222)
        smallfont = pygame.font.SysFont('Corbel', 35)
        self.text = smallfont.render('Następny cykl (spacja)', True, textColor)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        self.surface.blit(self.text, (self.x + self.width/6, self.y))

    def onClick(self, mouseX, mouseY):
        if self.isButtonClicked(mouseX, mouseY):
            self.simulation.runCycle()

    def isButtonClicked(self, mouseX, mouseY):
        return mouseX > self.x and mouseX < self.x + self.width and mouseY > self.y and mouseY < self.y + self.height