import unittest
import random

class RandomQueue:

    def __init__(self):
        self.item = []

    def insert(self, item):
        self.item.append(item)

    def remove(self):
        if self.is_empty():
            raise IndexError("Kolejka jest pusta")
        x = random.randint(0, len(self.item) - 1)# zwraca losowy element
        self.item[x], self.item[-1] = self.item[-1], self.item[x]
        return self.item.pop()

    def is_empty(self):
        return not self.item

    def is_full(self):
        return False

    def clear(self):
        self.item = []# czyszczenie listy

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.r_queue = RandomQueue()

    def test_insert(self):
        self.r_queue.insert(1)
        self.r_queue.insert(2)
        self.r_queue.insert(3)

        self.assertEqual(self.r_queue.item[0], 1)
        self.assertEqual(self.r_queue.item[1], 2)
        self.assertEqual(self.r_queue.item[2], 3)

    def test_remove(self):
        self.r_queue.insert(2)
        self.r_queue.insert(3)
        self.r_queue.insert(4)
        self.r_queue.insert(5)
        self.r_queue.insert(6)


        print(self.r_queue.remove())
        print(self.r_queue.remove())
        print(self.r_queue.remove())
        print(self.r_queue.remove())
        print(self.r_queue.remove())

if __name__ == '__main__':
    unittest.main()