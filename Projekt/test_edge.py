import unittest

from Edge import *


class EdgeTest(unittest.TestCase):
    def setUp(self):
        self.edge1 = Edge(0, 1, 17)
        self.edge2 = Edge(1, 2, 8)
        self.edge3 = Edge(2, 3, 2)

    def test__repr__(self):
        self.assertEqual(repr(self.edge1), "Edge(0, 1, 17)")
        self.assertEqual(repr(self.edge2), "Edge(1, 2, 8)")
        self.assertEqual(repr(self.edge3), "Edge(2, 3, 2)")

    def test_weight(self):
        self.assertTrue(self.edge1.weight == 17)
        self.assertTrue(self.edge2.weight == 8)
        self.assertTrue(self.edge3.weight == 2)

    def test_less_than(self):
        self.assertTrue(self.edge2 < self.edge1)
        self.assertTrue(self.edge3 < self.edge2)
        self.assertFalse(self.edge1 < self.edge2)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
