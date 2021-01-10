import unittest
#zad 9.1
class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

class SingleList:
        """Klasa reprezentująca całą listę jednokierunkową."""

        def __init__(self):
            self.length = 0  # nie trzeba obliczać za każdym razem
            self.head = None
            self.tail = None

        def is_empty(self):
            # return self.length == 0
            return self.head is None

        def count(self):  # tworzymy interfejs do odczytu
            return self.length

        def insert_head(self, node):
            if self.head:  # dajemy na koniec listy
                node.next = self.head
                self.head = node
            else:  # pusta lista
                self.head = self.tail = node
            self.length += 1

        def insert_tail(self, node):  # klasy O(N)
            if self.head:  # dajemy na koniec listy
                self.tail.next = node
                self.tail = node
            else:  # pusta lista
                self.head = self.tail = node
            self.length += 1

        def remove_head(self):  # klasy O(1)
            if self.is_empty():
                raise ValueError("pusta lista")
            node = self.head
            if self.head == self.tail:  # self.length == 1
                self.head = self.tail = None
            else:
                self.head = self.head.next
            node.next = None  # czyszczenie łącza
            self.length -= 1
            return node  # zwracamy usuwany node

        def remove_tail(self): # klasy O(N)
            # Zwraca cały węzeł, skraca listę.
            if self.is_empty():
                raise ValueError("pusta lista")
            node = self.tail
            if self.head == self.tail:  # self.length == 1
                self.head = self.tail = None
            else:
                temp = self.head
                while temp.next.next is not None:
                    temp = temp.next
                self.tail = temp
                self.tail.next = None
            node.next = None
            self.length -= 1
            return node


        def merge(self, other):
            # klasy O(1)
            # Węzły z listy other są przepinane do listy self na jej koniec.
            # Po zakończeniu operacji lista other ma być pusta.
            if self.is_empty():
                self.head = other.head
                self.length = other.length
                self.tail = other.tail
            if other.is_empty():
                return self.head
            else:
                self.tail.next = other.head
                self.tail = other.tail
                self.tail.next = None
                self.length = self.length + other.length
            other = None


        def clear(self): #czyszczenie tablicy
            """temp = self.head
            while self.head.next != None:
               self.head= self.head.next
               temp = None"""
            #tutaj nie wiem czy lepiej jest kontunuowac tak jak powyzej, kolejno wszystkie
            #czy wystarczy tak jak poniżej
            self.head = None
            self.tail = None
            self.length = 0

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.empty_list = SingleList()

        self.list1 = SingleList()
        self.list1.insert_head(Node(1))
        self.list1.insert_head(Node(2))
        self.list1.insert_tail(Node(3))
        self.list1.insert_tail(Node(6))
        self.list1.insert_tail(Node(9))
        self.list1.insert_tail(Node(10))
        self.list1.insert_head(Node(100))
        # Tak wyglada lista po powyższych operacjach: [100, 2, 1, 3, 6, 9, 10]

        self.list2 = SingleList()
        self.list2.insert_head(Node(0))
        self.list2.insert_head(Node(1))
        self.list2.insert_head(Node(2))
        self.list2.insert_head(Node(3))
        #Tak wyglada lista po powyższych operacjach: [3, 2, 1, 0]

    def test_remove_tail(self):
        self.assertEqual(self.list1.remove_tail().data, 10)
        self.assertEqual(self.list2.remove_tail().data, 0)
        # dla pustej listy
        with self.assertRaises(ValueError):
            self.empty_list.remove_tail()

    def test_merge(self):
        self.list1.merge(self.list2)
        self.assertEqual(
            self.list1.length, 11)
        self.assertEqual(self.list1.head.data, 100)
        self.assertEqual(self.list1.tail.data, 0)
        #Dla pustej listy
        self.empty_list.merge(self.list2)
        self.assertEqual(self.empty_list.head.data, 3)
        self.assertEqual(self.empty_list.tail.data, 0)

    def test_clear(self):
        self.list1.clear()
        self.assertEqual(self.list1.head, None)
        self.assertEqual(self.list1.tail, None)


if __name__ == '__main__':
    unittest.main()
