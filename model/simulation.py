from model import cell


class Simulation:
    def __init__(self, width, height):
        self.cellTable = [0] * width
        for i in range(width):
            self.cellTable[i] = [0] * height
            for j in range(height):
                self.cellTable[i][j] = cell.Cell(i, j)

    def runCycle(self):
        for x in range(len(self.cellTable)):
            for y in range(len(self.cellTable[x])):
                self.cellTable[x][y].calculateNextCycle(self.cellTable)

        # actually changing the state in a separate loop so that it won't affect the state calculations
        for x in range(len(self.cellTable)):
            for y in range(len(self.cellTable[x])):
                self.cellTable[x][y].alive = self.cellTable[x][y].nextCycleAlive

    def setCellState(self, state, x, y):
        self.cellTable[x][y].alive = state
