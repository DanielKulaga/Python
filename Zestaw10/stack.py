import unittest


class Stack:

    def __init__(self, size=10):
        self.items = size * [None]      # utworzenie tablicy
        self.n = 0                      # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise ValueError("Stos jest zapełniony!")
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        if self.is_empty():
            raise ValueError("Stos jest pusty!")
        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None
        return data


class Test_Stack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack(3)
        self.stack1 = Stack(1)
        self.stack1.push(2)

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.assertFalse(self.stack1.is_empty())

    def test_push(self):
        self.stack.push(3)
        self.assertEqual(self.stack.n, 1)
        self.assertEqual(self.stack.items[0], 3)
        self.stack.push(100)
        self.assertEqual(self.stack.n, 2)
        self.assertEqual(self.stack.items[0], 3)
        self.assertEqual(self.stack.items[1], 100)

        self.assertFalse(self.stack.is_empty())
        self.stack.push(4)
        try:
            self.stack.push(10)
        except Exception as exception:
            self.assertEqual(ValueError, exception.__class__)

    def test_pop(self):
        self.stack.push(4)
        self.stack.push(100)
        self.stack.push(3)
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 100)
        self.assertEqual(self.stack.pop(), 4)

        try:
            self.stack.pop()
        except Exception as exception1:
            self.assertEqual(ValueError, exception1.__class__)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
