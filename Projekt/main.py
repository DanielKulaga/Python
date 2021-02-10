from Graph import *


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



















