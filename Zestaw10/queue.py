import unittest


class Queue:

    def __init__(self, size=5):
        self.n = size + 1         # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0           # pierwszy do pobrania
        self.tail = 0           # pierwsze wolne

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n-1) % self.n == self.tail

    def put(self, data):
        if self.is_full():
            raise ValueError("Kolejka jest pełna!")
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):
        if self.is_empty():
            raise ValueError("Kolejka jest pusta!")
        data = self.items[self.head]
        self.items[self.head] = None      # usuwam referencję
        self.head = (self.head + 1) % self.n
        return data


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.queue = Queue(4)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())

    def test_put(self):
        self.queue.put(3)
        self.assertEqual(self.queue.n, 5)
        self.assertEqual(self.queue.items[0], 3)
        self.queue.put(2)
        self.assertEqual(self.queue.n, 5)
        self.assertEqual(self.queue.items[0], 3)
        self.assertEqual(self.queue.items[1], 2)

        self.assertFalse(self.queue.is_empty())

        try:
            self.queue.put(100)
        except Exception as exception:
            self.assertEqual(ValueError, exception.__class__)

    def test_get(self):
        self.queue.put(8)
        self.queue.put(9)
        self.queue.put(13)
        self.assertEqual(self.queue.get(), 8)
        self.assertEqual(self.queue.get(), 9)
        self.assertEqual(self.queue.get(), 13)

        try:
            self.queue.get()
        except Exception as exception:
            self.assertEqual(ValueError, exception.__class__)

    


if __name__ == '__main__':
    unittest.main()