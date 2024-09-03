class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = False

    def calculateNextCycle(self, cellTable):
        aliveCount = 0

        # left upper corner of the cell
        if self.x != 0 and self.y != 0:
            if cellTable[self.x - 1][self.y - 1].alive:
                aliveCount += 1
        # right upper corner of the cell
        if self.x != len(cellTable) - 1 and self.y != 0:
            if cellTable[self.x +1 ][self.y - 1].alive:
                aliveCount += 1
        # left down corner of the cell
        if self.x != 0 and self.y != len(cellTable[self.x]) - 1:
            if cellTable[self.x - 1][self.y + 1].alive:
                aliveCount += 1
        # right down corner of the cell
        if self.x != len(cellTable) -1 and self.y != len(cellTable[self.x]) - 1:
            if cellTable[self.x + 1][self.y + 1].alive:
                aliveCount += 1
        # left side of the cell
        if self.x != 0:
            if cellTable[self.x-1][self.y].alive:
                aliveCount += 1
        # right side of the cell
        if self.x != len(cellTable) - 1:
            if cellTable[self.x+1][self.y].alive:
                aliveCount += 1
        # above the cell
        if self.y != 0:
            if cellTable[self.x][self.y-1].alive:
                aliveCount += 1
        # under the cell
        if self.y != len(cellTable[self.x]) - 1:
            if cellTable[self.x][self.y+1].alive:
                aliveCount += 1



        if not self.alive:
            if aliveCount == 3:
                self.nextCycleAlive = True
            else:
                self.nextCycleAlive = False

        if self.alive:
            if aliveCount == 2 or aliveCount == 3:
                self.nextCycleAlive = True
            else:
                self.nextCycleAlive = False