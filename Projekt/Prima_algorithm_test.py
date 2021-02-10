import unittest
from Graph import *

from PriorityQueue import *

class PrimaTestCase(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

        self.graph.add_edge_undirected(Edge('A', 'C', 2))
        self.graph.add_edge_undirected(Edge('A', 'D', 5))
        self.graph.add_edge_undirected(Edge('B', 'A', 6))
        self.graph.add_edge_undirected(Edge('F', 'C', 1))
        self.graph.add_edge_undirected(Edge('E', 'C', 2))
        self.graph.add_edge_undirected(Edge('E', 'F', 6))
        self.graph.add_edge_undirected(Edge('D', 'E', 3))
        self.graph.add_edge_undirected(Edge('B', 'F', 3))
        self.selected_node = 'A'

        self.graph1 = Graph()
        self.graph1 = self.graph.PrimAlgorithm(self.selected_node)

    #Spodziewany wygląd minimalnego drzewa rozpinającego
    def test_prima_algorithm(self):
        self.assertEqual(list(self.graph1.generator_node_edges('A')), [('A', 'C', 2)])
        self.assertEqual(list(self.graph1.generator_node_edges('B')), [('B', 'F', 3)])
        self.assertEqual(list(self.graph1.generator_node_edges('C')), [('C', 'A', 2), ('C', 'F', 1), ('C', 'E', 2)])
        self.assertEqual(list(self.graph1.generator_node_edges('D')), [('D', 'E', 3)])
        self.assertEqual(list(self.graph1.generator_node_edges('E')), [('E', 'C', 2), ('E', 'D', 3)])
        self.assertEqual(list(self.graph1.generator_node_edges('F')), [('F', 'C', 1), ('F', 'B', 3)])

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()
