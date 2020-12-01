import unittest
from Circle import *
from Point import *

class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle1 = Circle(5, 4, 6)
        self.circle2 = Circle(2, 6, 1)
        self.circle3 = Circle(5, 8, 6)
        self.circle4 = Circle(4, 3, 2)
        self.circle5 = Circle(8, 4, 2)
        self.circle6 = Circle(10, 3, 3)
        self.circle7 = Circle(5, 8, 6)
        self.circle8 = Circle(1, 2, 5)
        self.circle9 = Circle(-1, 2, 5)
        self.circle10 = Circle(0, 4, 7)
        self.circle11 = Circle(3, -2, 8)

    def test_equal(self):
        self.assertFalse(self.circle1 == self.circle2)
        self.assertTrue(self.circle1 == Circle(5, 4, 6))
        self.assertTrue(self.circle2 == Circle(2, 6, 1))
        self.assertTrue(self.circle3 == Circle(5, 8, 6))
        self.assertFalse(self.circle4 == self.circle3)

    def test_cover(self):
        self.assertEqual(Circle(0, 2, 6.0), self.circle8.cover(self.circle9))
        self.assertEqual(Circle(0, 3, 8.0), self.circle9.cover(self.circle10))
        self.assertEqual(Circle(1, 0, 10.83), self.circle10.cover(self.circle11))

    def test_area(self):
        self.assertAlmostEqual(self.circle1.area(), 113.09724)
        self.assertEqual(self.circle2.area(), 3.14159)
        self.assertEqual(self.circle4.area(), 12.56636)
        self.assertAlmostEqual(self.circle6.area(), 28.27431)

    def test_move(self):
        self.assertEqual(self.circle1.move(2, 3), Circle(7, 7, 6))
        self.assertEqual(self.circle3.move(-2, -3), Circle(3, 5, 6))
        self.assertEqual(self.circle4.move(4, 1), Circle(8, 4, 2))
        self.assertEqual(self.circle5.move(6, 2), Circle(14, 6, 2))
        self.assertEqual(self.circle6.move(0, 5), Circle(10, 8, 3))

if __name__ == '__main__':
    unittest.main()
