import unittest
from heapq import *
import sys

class QueueItem:
    def __init__(self, source, target, priority):
        self.source = source
        self.target = target
        self._priority = priority
        self.queue = None


    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        self._priority = priority
        self.queue.rebuild_queue()

    def set_queue(self, queue):
        self.queue= queue

    def __int__(self):
        return self.priority

    def __lt__(self, other):
        return self._priority < other.priority

    def __str__(self):
        return "Edge({}, {}, {})".format(
            self.source, self.target, self.priority)


class PriorityQueue:
    def __init__(self):
        self.queue=[]

    def enqueue(self, item: QueueItem):
        heappush(self.queue, item)
        item.set_queue(self)
        return self

    def rebuild_queue(self):
        heapify(self.queue)

    def dequeue(self):
        return heappop(self.queue)

    def __iter__(self):
        return iter(self.queue)

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        L = list()
        for item in self.queue:
            L.append("{} ".format(str(item)))
        return "".join(L)


class Edge:
    """Klasa krawędzi (okreslanie wagi,wierzchołki poczatkowe i koncowe krawedzi)"""
    def __init__ (self, start_node, end_node, weight = 1):
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight

    def __repr__(self):
        if self.weight == 1:
            return "Edge({}, {})".format(repr(self.start_node), repr(self.end_node))
        else:
            return "Edge({}, {}, {})".format(
                repr(self.start_node), repr(self.end_node), repr(self.weight))


class Graph:
    """Słownikowa reprezentacja grafu"""
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        """Wstawia wierzchołek do grafu."""
        if node not in self.graph:
            self.graph[node] = {}

    def add_edge_undirected(self, edge):
        """Dodaje krawędź do grafu nieskierowanego."""
        source = edge.start_node
        weight = edge.weight
        target = edge.end_node

        self.add_node(source)
        self.add_node(target)
        # Możemy wykluczyć pętle.
        if source == target:
            raise ValueError("pętle są zabronione")
        if target not in self.graph[source]:
            self.graph[source][target] = weight
        if source not in self.graph[target]:
            self.graph[target][source] = weight

    def list_nodes(self):
        """Zwraca listę wierzchołków grafu."""
        return self.graph.keys()

    def list_edges(self):
        """Zwraca listę krawędzi (3-krotek) grafu skierowanego ważonego."""
        L = []
        for source in self.graph:
            for target in self.graph[source]:
                L.append((source, target, self.graph[source][target]))
        return L

    def list_node_edges(self, node):
        """Zwraca liste krawedzi konkretnego wierzchołka"""
        L = []
        for source in self.graph:
            if source == node:
                for target in self.graph[source]:
                    L.append((source, target, self.graph[source][target]))
        return L

    def graph_size(self):
        return len(self.list_nodes())

    def print_graph(self):
        """Wypisuje postać grafu nieskierowanego ważonego na ekranie."""
        L = []
        for source in self.graph:
            L.append("{} : ".format(source))
            for target in self.graph[source]:
               L.append("{}({}) ".format(target, self.graph[source][target]))
            L.append("\n")
        print("".join(L))

    def PrimAlgorithm(self, selected_node):
        # Ilosc wierzchołków w grafie
        numOfVerticles = self.graph_size()

        mst = Graph()
        
        visited = dict()
        for n in self.list_nodes():
            visited[n] = False
        #vertex = visited[0]
        visited[selected_node] = True
        Edges = PriorityQueue()
        ab = self.list_node_edges(selected_node)
        for edge in ab:
            Edges.enqueue(QueueItem(edge[0], edge[1], edge[2]))



        while mst.graph_size() != self.graph_size():
            queue_item = Edges.dequeue()
           # print(mst.list_nodes())
            #print(queue_item.target)
            # print(mst.graph_size())
            if visited[queue_item.target] == False:
                mst.add_edge_undirected(Edge(queue_item.source, queue_item.target, queue_item.priority))
                #mst.print_graph()
                visited[queue_item.target] = True

                ab = self.list_node_edges(queue_item.target)
                for edge in ab:
                    Edges.enqueue(QueueItem(edge[0], edge[1], edge[2]))

        return mst



graph = Graph()

print("Witaj w programie generującym minimalne drzewo rozpinające algorytmem Prima ")
chosen = input("Wybierz: A - gotowy graf, B- chce podać swoj graf : ")
if chosen == 'A' or chosen == 'a':
    graph.add_edge_undirected(Edge('A', 'C', 2))
    graph.add_edge_undirected(Edge('A', 'D', 5))
    graph.add_edge_undirected(Edge('B', 'A', 6))
    graph.add_edge_undirected(Edge('F', 'C', 1))
    graph.add_edge_undirected(Edge('E', 'C', 2))
    graph.add_edge_undirected(Edge('E', 'F', 6))
    graph.add_edge_undirected(Edge('D', 'E', 3))
    graph.add_edge_undirected(Edge('B', 'F', 3))
    print("\n Oto gotowy graf")
    graph.print_graph()
    selected_node = input("\nPodaj od którego z powyższych wierzchołków ma zacząc algorytm: ")

    mst = graph.PrimAlgorithm(selected_node)
    mst.print_graph()

elif chosen == 'B' or chosen =='b':
    num_of_edges = input("Podaj ilość krawedzi twojego grafu spójnego i ważonego: ")
    for i in range(0, int(num_of_edges)):
        x, y, z = input(
            "Podaj dane krawędzi: wierzcholek_startowy(spacja)wierzcholek_koncowy(spacja)waga_krawedzi ").split()
        graph.add_edge_undirected(Edge(x, y, int(z)))
    print('\n')
    graph.print_graph()
    selected_node = input("\nPodaj od którego z powyższych wierzchołków ma zacząc algorytm: ")
    mst1 = graph.PrimAlgorithm(selected_node)
    mst1.print_graph()
else:
    print("Wprowadzono niepoprawny znak, podaj 'a' lub 'b'.")




















