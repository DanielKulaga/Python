
class Edge:
    """Klasa krawędzi (okreslanie wagi,wierzchołki poczatkowe i koncowe krawedzi)"""
    def __init__ (self, start_node, end_node, weight = 1):
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight
        self.queue = None

    def __repr__(self):
        """Reprezentacja krawędzi"""
        if self.weight == 1:
            return "Edge({}, {})".format(repr(self.start_node), repr(self.end_node))
        else:
            return "Edge({}, {}, {})".format(
                repr(self.start_node), repr(self.end_node), repr(self.weight))

    def __lt__(self, other):
        """Porównanie wagi krawędzi"""
        return self.weight < other.weight

    def set_queue(self, queue):
        self.queue = queue

