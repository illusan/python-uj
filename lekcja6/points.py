# ZADANIE 6.2
# W pliku points.py zdefiniować klasę Point wraz z potrzebnymi metodami.
# Punkty są traktowane jak wektory zaczepione w początku układu współrzędnych,
# o końcu w położeniu (x, y). Napisać kod testujący moduł points.


import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def cross(self, other):
        return self.x * other.y - self.y * other.x

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __hash__(self):
        return hash((self.x, self.y))


import unittest


class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(3, 4)

    def test_str(self):
        self.assertEqual(str(self.p1), "(1, 2)")

    def test_repr(self):
        self.assertEqual(repr(self.p1), "Point(1, 2)")

    def test_eq(self):
        self.assertEqual(self.p1 == Point(1, 2), True)
        self.assertEqual(self.p1 == self.p2, False)

    def test_ne(self):
        self.assertEqual(self.p1 != self.p2, True)
        self.assertEqual(self.p1 != Point(1, 2), False)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(4, 6))

    def test_sub(self):
        self.assertEqual(self.p2 - self.p1, Point(2, 2))

    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, 11)

    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p2), -2)

    def test_length(self):
        self.assertEqual(self.p2.length(), 5.0)

    def test_hash(self):
        self.assertEqual(hash(self.p1), hash(Point(1, 2)))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
