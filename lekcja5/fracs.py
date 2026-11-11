# ZADANIE 5.2
# Stworzyć plik fracs.py i zapisać w nim funkcje do działań na ułamkach.
# Ułamek będzie reprezentowany przez listę dwóch liczb całkowitych [licznik, mianownik].
# Napisać kod testujący moduł fracs. Nie należy korzystać z klasy Fraction z modułu fractions.
# Można wykorzystać funkcję fractions.gcd() [Py2, zwraca liczby dodatnie lub ujemne]
# lub math.gcd() [Py3, zwraca liczby nieujemne] implementującą algorytm Euklidesa.


from math import gcd


def skroc(frac):
    if frac[1] == 0:
        raise ValueError("mianownik nie moze byc zerem")
    d = gcd(frac[0], frac[1])
    licznik = frac[0] // d
    mianownik = frac[1] // d
    if mianownik < 0:
        licznik = -licznik
        mianownik = -mianownik
    return [licznik, mianownik]


def add_frac(frac1, frac2):
    licznik = frac1[0] * frac2[1] + frac2[0] * frac1[1]
    mianownik = frac1[1] * frac2[1]
    return skroc([licznik, mianownik])


def sub_frac(frac1, frac2):
    licznik = frac1[0] * frac2[1] - frac2[0] * frac1[1]
    mianownik = frac1[1] * frac2[1]
    return skroc([licznik, mianownik])


def mul_frac(frac1, frac2):
    return skroc([frac1[0] * frac2[0], frac1[1] * frac2[1]])


def div_frac(frac1, frac2):
    frac2 = skroc(frac2)
    if frac2[0] == 0:
        raise ValueError("nie mozna dzielic przez zero")
    return skroc([frac1[0] * frac2[1], frac1[1] * frac2[0]])


def is_positive(frac):
    return frac[0] * frac[1] > 0


def is_zero(frac):
    return frac[0] == 0


def cmp_frac(frac1, frac2):
    roznica = sub_frac(frac1, frac2)
    if is_zero(roznica):
        return 0
    if is_positive(roznica):
        return 1
    return -1


def frac2float(frac):
    return frac[0] / frac[1]


import unittest


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 2], [-1, 2]), self.zero)

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([3, 1], [6, 2]), self.zero)

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [2, 3]), [1, 3])
        self.assertEqual(mul_frac([-1, 2], [1, -2]), [1, 4])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([1, 2], [-1, 4]), [-2, 1])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([1, -2]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 2]), True)
        self.assertEqual(is_zero([1, 2]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([-1, 2], [1, -2]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([6, 2]), 3.0)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()