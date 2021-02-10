import unittest

from PriorityQueue import *
from Edge import *


class PriorityQueueTest(unittest.TestCase):
    def setUp(self):
        self.pq1 = PriorityQueue()

    def test_enqueue(self):
        self.pq1.enqueue(Edge(2, 4, 18))
        self.assertEqual(str(self.pq1), "Edge(2, 4, 18) ")
        self.pq1.enqueue(Edge(2, 9, 12))
        self.assertEqual(str(self.pq1), "Edge(2, 9, 12) Edge(2, 4, 18) ")


    def test_str(self):
        self.pq1.enqueue(Edge(2, 4, 18))
        self.assertEqual(str(self.pq1), "Edge(2, 4, 18) ")

    def test_dequeue(self):
        self.pq1.enqueue(Edge(2, 4, 18))
        self.pq1.enqueue(Edge(3, 8, 20))
        self.pq1.enqueue(Edge(3, 8, 7))
        self.assertEqual(repr(self.pq1.dequeue()), "Edge(3, 8, 7)")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
