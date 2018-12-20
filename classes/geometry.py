class Point:
    """"""

    def __init__(self, x, y):
        """"""

        self.x, self.y = x, y

    def tuple(self):
        """"""
        
        return (self.x, self.y)

    def clone(self):
        """"""

        return Point(self.x, self.y)

class Rectangle:
    """"""

    def __init__(self, pos, tx, ty):
        """"""

        self._pos = pos
        self._tx = tx
        self._ty = ty

    def contains(self, point):
        """"""

        in_x = point.x >= self._pos.x and point.x <= self._pos.x + self._tx
        in_y = point.y >= self._pos.y and point.y <= self._pos.y + self._ty
        return in_x and in_y
    
    def tx(self):
        """"""

        return self._tx

    def ty(self):
        """"""

        return self._ty
