from point import Point
class Universe:
    listOfLiveCells = set([])
    def getCellAt(__self__, x, y):
        return Point(x,y) in __self__.listOfLiveCells

    def __init__(__self__, locationOfLiveCells=None):
        if locationOfLiveCells:
            for cell in locationOfLiveCells:
                __self__.listOfLiveCells.add(Point(cell[0], cell[1]))
