class DirectedGraph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node] = []

    def add_edge(self, nodeA, nodeB):
        if nodeA not in self.nodes:
            self.add_node(nodeA)
        if nodeB not in self.nodes:
            self.add_node(nodeB)
        if nodeB not in self.nodes[nodeA]:
            self.nodes[nodeA].append(nodeB)

    def get_neighbors_for(self, node):
        if node not in self.nodes:
            print("Ther's no such node!")
        else:
            print(self.nodes[node])

    def path_between(self, nodeA, nodeB, p=[]):
        path = []
        path += p
        path += nodeA
        if nodeA == nodeB:
            return path
        if nodeA not in self.nodes:
            return False
        for node in self.nodes[nodeA]:
            if node not in path:
                new_path = self.path_between(node, nodeB, path)
                if new_path:
                    return new_path
        return False

    def toString(self):
        for node in self.nodes:
            print("%s:" % node)
            self.get_neighbors_for(node)


def main():
    my_graph = DirectedGraph()
    my_graph.add_node("A")
    my_graph.add_node("B")
    my_graph.add_node("C")
    my_graph.add_node("D")
    my_graph.add_node("E")
    my_graph.add_node("F")
    my_graph.add_edge("A", "B")
    my_graph.add_edge("B", "C")
    my_graph.add_edge("A", "D")
    my_graph.add_edge("C", "A")
    my_graph.add_edge("C", "E")
    my_graph.add_edge("C", "F")
    my_graph.add_edge("D", "W")
    print(my_graph.path_between("A", "W"))
    my_graph.toString()


if __name__ == '__main__':
    main()
