from ui import cellTile
import pygame

class cellBoard:
    def __init__(self, simulation):
        self.surface = pygame.display.set_mode((800,600))
        self.simulation = simulation
        cellWidth = 20
        cellHeight = 20
        padding = 5
        cellTable = simulation.cellTable
        self.board = [0] * len(cellTable)
        for i in range(len(cellTable)):
            self.board[i] = [0] * len(cellTable[i])
            for j in range(len(cellTable[i])):
                self.board[i][j] = cellTile.cellTile(i * cellWidth + i * padding, j * cellHeight + j * padding, cellTable[i][j], self.surface)

    def draw(self):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                self.board[x][y].draw()

    def onClick(self, mouseX, mouseY):
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                if self.isCellTileClicked(self.board[x][y], mouseX, mouseY):
                    self.board[x][y].cell.alive = not self.board[x][y].cell.alive

    def isCellTileClicked(self, cellTile, mouseX, mouseY):
        return mouseX > cellTile.x and mouseX < cellTile.x+cellTile.width and mouseY > cellTile.y and mouseY < cellTile.y+cellTile.height