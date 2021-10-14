class GraphNode:

    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None


a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
c.neighbors.add(b)

graph = [a, b, c]


def color_graph(graph, colors):
    for node in graph:
        if node in node.neighbors:
            raise Exception(f"legal coloring impossible for node with loop: {node.lable}")
        
        illegal_colors = set([
            neighbor.color
            for neighbor in node.neighbors
            if neighbor.color
        ])
        for color in colors:
            if color not in illegal_colors:
                node.color = color
                break