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

        self.pos = pos
        self._tx = tx
        self._ty = ty
    
    def tx(self):
        """"""

        return self._tx

    def ty(self):
        """"""

        return self._ty

    def contains(self, point):
        """"""

        in_x = point.x >= self.pos.x and point.x <= self.pos.x + self._tx
        in_y = point.y >= self.pos.y and point.y <= self.pos.y + self._ty
        return in_x and in_y

    def intersects(self, rect):
        """"""

        a = self.contains(rect.pos) or self.contains(Point(rect.pos.x + rect.tx(), rect.pos.y))
        b = self.contains(Point(rect.pos.x, rect.pos.y + rect.ty())) or self.contains(Point(rect.pos.x + rect.tx(), rect.pos.y + rect.ty()))
        return a or b
