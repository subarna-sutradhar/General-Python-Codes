"""Inheritance: is the pillars of object oriented programing(incapsulation)"""
"""WITHOUT USING SUPER"""
class Square:
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side * self.side

class Cube(Square):
    def area(self):
        face_area = self.side * self.side
        return face_area * 6

    def volume(self):
        face_area = self.side * self.side
        return face_area * self.side

#s = Square(9)
#s.area()