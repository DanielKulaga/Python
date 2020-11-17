#Zadanie 5.2
import math
import unittest
from fracs import *


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]
        self.f1 = [-1, 2]
        self.f2 = [0, 1]
        self.f3 = [3, 1]
        self.f4 = [6, 2]
        self.f5 = [0, 2]
        self.f7 = [1, 6]
        self.f8 = [10, 1]
        self.f9 = [100, 2]
        self.f10 = [6, 2]

    def test_add_frac(self):
        self.assertEqual(add_frac(self.f3, self.f4), [6, 1])
        self.assertEqual(add_frac(self.f4, self.f7), [19, 6])
        self.assertEqual(add_frac(self.f5, self.f7), [1, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.f8, self.f4), [7, 1])
        self.assertEqual(sub_frac(self.f9, self.f3), [47, 1])

    def test_mul_frac(self):
        self.assertEqual(mul_frac(self.f8, self.f4), [30, 1])
        self.assertEqual(mul_frac(self.f9, self.f2), [0, 1])

    def test_div_frac(self):
        self.assertEqual(div_frac(self.f9, self.f2), ZeroDivisionError)
        self.assertEqual(div_frac(self.f7, self.f3), [1, 18])

    def test_is_positive(self):
        self.assertEqual(is_positive(self.f7), True)
        self.assertEqual(is_positive(self.f1), False)
        self.assertEqual(is_positive(self.f4), True)

    def test_is_zero(self):
        self.assertEqual(is_zero(self.zero), True)
        self.assertEqual(is_zero(self.f7), False)
        self.assertEqual(is_zero(self.f4), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.f4, self.f7), 1)
        self.assertEqual(cmp_frac(self.f3, self.f9), -1)
        self.assertEqual(cmp_frac(self.f4, self.f10), 0)


    def test_frac2float(self):
        self.assertAlmostEqual(frac2float(self.f9), 50)
        self.assertAlmostEqual(frac2float(self.f10), 3)
        self.assertAlmostEqual(frac2float(self.f5), 0)
        assert isinstance(frac2float(self.f9), float) == True

    def tearDown(self):
        self.assertEqual(function_gcd(self.f10),[3, 1])

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
