import pygame
from ui import cellBoard, nextCycleButton

from model import simulation


class Window:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Gra w życie')
        background = pygame.Surface((800, 600))
        background.fill(pygame.Color('#000000'))

        self.simulation = simulation.Simulation(16, 16)
        board = cellBoard.cellBoard(self.simulation)
        button = nextCycleButton.NextCycleButton(100, 500, self.simulation)
        self.items = []
        self.items.append(board)
        self.items.append(button)


    def run(self):
        is_running = True
        for i in range(len(self.items)):
            self.items[i].draw()
        pygame.display.update()
        while is_running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.simulation.runCycle()
                        for i in range(len(self.items)):
                            self.items[i].draw()
                            pygame.display.update()

                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_presses = pygame.mouse.get_pressed()
                    if mouse_presses[0]:
                        mouse = pygame.mouse.get_pos()
                        for i in range(len(self.items)):
                            self.items[i].onClick(mouse[0], mouse[1])
                        for i in range(len(self.items)):
                            self.items[i].draw()
                            pygame.display.update()