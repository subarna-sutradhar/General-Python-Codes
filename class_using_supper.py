"""USING SUPER"""
class Square:
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side * self.side

class Cube(Square):
    def area(self):
        return super().area() * 6 #"""super calls the area of Square class"""
    def volume(self):
        return super().area() * self.side