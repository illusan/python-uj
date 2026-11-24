# ZADANIE 6.3
# W pliku rectangles.py zdefiniować klasę Rectangle wraz z potrzebnymi metodami.
# Prostokąt jest określony przez podanie dwóch wierzchołków klasy Point,
# lewego dolnego (pt1) i prawego górnego (pt2). Boki prostokąta są równoległe
# do osi układu współrzędnych. Napisać kod testujący moduł rectangles.


from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return f"[{self.pt1}, {self.pt2}]"

    def __repr__(self):
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point((self.pt1.x + self.pt2.x) / 2, (self.pt1.y + self.pt2.y) / 2)

    def area(self):
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):
        self.pt1 = self.pt1 + Point(x, y)
        self.pt2 = self.pt2 + Point(x, y)


import unittest


class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rect = Rectangle(0, 0, 4, 2)

    def test_str(self):
        self.assertEqual(str(self.rect), "[(0, 0), (4, 2)]")

    def test_repr(self):
        self.assertEqual(repr(self.rect), "Rectangle(0, 0, 4, 2)")

    def test_eq(self):
        self.assertEqual(self.rect == Rectangle(0, 0, 4, 2), True)
        self.assertEqual(self.rect == Rectangle(0, 0, 3, 3), False)

    def test_ne(self):
        self.assertEqual(self.rect != Rectangle(0, 0, 3, 3), True)
        self.assertEqual(self.rect != Rectangle(0, 0, 4, 2), False)

    def test_center(self):
        self.assertEqual(self.rect.center(), Point(2, 1))

    def test_area(self):
        self.assertEqual(self.rect.area(), 8)

    def test_move(self):
        self.rect.move(1, 3)
        self.assertEqual(self.rect, Rectangle(1, 3, 5, 5))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
