
from heapq import *
from Edge import *

class PriorityQueue:
    """Klasa reprezentujaca kolejkę priorytetową"""
    def __init__(self):
        self.queue = []

    def enqueue(self, item: Edge):
        """Metoda dodająca element do kolejki priorytetowej"""
        heappush(self.queue, item)
        #item.set_queue(self)
        return self


    def rebuild_queue(self):
        """Przbudowuje, aby spelnialo warunek kopca"""
        heapify(self.queue)

    def dequeue(self):
        """Usuwa element z kolejki"""
        return heappop(self.queue)

    def __iter__(self):
        """Iteracja po kolejnych elementach"""
        return iter(self.queue)

    def __len__(self):
        """Zwraca dlugosc kolejki"""
        return len(self.queue)

    def __str__(self):
        "Wypisuje kolejkę"
        L = list()
        for item in self.queue:
            L.append("{} ".format(str(item)))
        return "".join(L)
