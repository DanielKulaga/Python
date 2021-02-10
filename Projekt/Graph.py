
from PriorityQueue import *

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
            raise ValueError("Wystąpiła pętla")
        if target not in self.graph[source]:
            self.graph[source][target] = weight
        if source not in self.graph[target]:
            self.graph[target][source] = weight

    def list_nodes(self):
        """Zwraca listę wierzchołków grafu."""
        return list(self.graph.keys())


    def generator_node_edges(self, node):
        """Zwraca liste krawedzi konkretnego wierzchołka"""
        for source in self.graph:
            if source == node:
                for target in self.graph[source]:
                    yield source, target, self.graph[source][target]


    def graph_size(self):
        """Zwraca rozmiar grafu"""
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
        """Matoda reprezentująca algorytm prima"""

        mst = Graph()

        """odwiedzone wierzcholki """
        visited = dict()
        for n in self.list_nodes():
            visited[n] = False
       #Zmiana wartosci w odwiedzonej (wybranej przez usera)
        visited[selected_node] = True
        Edges = PriorityQueue()
        #generuje krawedzie ktore wychodza z danego wierzcholka
        edges_in_node = self.generator_node_edges(selected_node)
        for edge in edges_in_node:
            Edges.enqueue(Edge(edge[0], edge[1], edge[2]))

        while mst.graph_size() != self.graph_size():
            queue_item = Edges.dequeue()

            if visited[queue_item.end_node] == False:
                mst.add_edge_undirected(Edge(queue_item.start_node, queue_item.end_node, queue_item.weight))

                visited[queue_item.end_node] = True

                edges_in_node = self.generator_node_edges(queue_item.end_node)
                for edge in edges_in_node:
                    Edges.enqueue(Edge(edge[0], edge[1], edge[2]))

        return mst
