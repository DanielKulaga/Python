import unittest


from Graph import *


class GraphTest(unittest.TestCase):
    def setUp(self):
        self.graph1 = Graph()

        self.graph2 = Graph()

        self.graph3 = Graph()
        self.graph3.add_edge_undirected(Edge('A', 'B', 10))
        self.graph3.add_edge_undirected(Edge('B', 'C', 11))
        self.graph3.add_edge_undirected(Edge('C', 'D', 12))
        self.graph3.add_edge_undirected(Edge('D', 'A', 13))


    def test_graphsize(self):
        self.graph1.add_node(0)
        self.graph1.add_node(1)
        self.graph1.add_node(2)
        self.graph1.add_node(3)
        self.assertEqual(self.graph1.graph_size(), 4)

    def test_list_node_edges(self):
        self.assertEqual(list(self.graph3.generator_node_edges('A')), [('A', 'B', 10), ('A', 'D', 13)])

    def test_list_nodes(self):
        self.graph1.add_node('A')
        self.graph1.add_node('B')
        self.graph1.add_node('C')
        self.graph1.add_node('D')

        self.assertEqual(self.graph1.list_nodes(), (['A', 'B', 'C', 'D']))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
