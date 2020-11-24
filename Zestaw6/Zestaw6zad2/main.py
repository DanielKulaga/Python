#Unit tests for fracs
import unittest
from fracs import *

class TestFractions(unittest.TestCase):

    def setUp(self):
     self.zero = Frac(0, 1)
     self.f1 = Frac(-1, 2)
     self.f2 = Frac(0, 1)
     self.f3 = Frac(3, 1)
     self.f4 = Frac(6, 2)
     self.f5 = Frac(0, 2)
     self.f6 = Frac(9, 2)
     self.f7 = Frac(1, 6)
     self.f8 = Frac(10, 1)
     self.f9 = Frac(100, 2)
     self.f10 = Frac(6, 2)

    def test_add(self):
        self.assertEqual(Frac(1, 1) + Frac(2, 2), Frac(2, 1))
        self.assertEqual(self.f4 + self.f7, Frac(19, 6))
        self.assertEqual(self.f5 + self.f7, Frac(1, 6))



    def test_sub(self):
        self.assertEqual(self.f8 - self.f4, Frac(7, 1))
        self.assertEqual(self.f9 - self.f3, Frac(47, 1))

    def test_mul(self):
        self.assertEqual(self.f8 * self.f4, Frac(30, 1))
        self.assertEqual(self.f9 * self.f2, Frac(0, 1))


    def test_div(self):
        self.assertEqual(self.f9 / self.f2, ZeroDivisionError)
        self.assertEqual(self.f7 / self.f3, Frac(1, 18))

    def test_pos(self):
        self.assertEqual(+(self.f2), Frac(0, 1))
        self.assertEqual(+(self.f1), Frac(1, 2))

    def test_invert(self):
        self.assertEqual(~(self.f2),Frac(1, 0))
        self.assertEqual(~(self.f8),Frac(1, 10))


    def test_cmp_frac(self):
        self.assertEqual(self.f2 < self.f4, True)
        self.assertEqual(self.f5 < self.f2, False)
        self.assertEqual(self.f6 < self.f6, False)
        self.assertEqual(self.f4 < self.f8, True)
        self.assertEqual(self.f9 < self.f8, False)

    def test_frac2float(self):
        self.assertAlmostEqual(float(self.f9), 50)
        self.assertAlmostEqual(float(self.f10), 3)
        self.assertAlmostEqual(float(self.f5), 0)
        assert isinstance(float(self.f9), float) == True

    def test_print(self):
        self.assertEqual(str(self.f1), "-1/2")
        self.assertEqual(str(Frac(99999, 1)), "99999")


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
