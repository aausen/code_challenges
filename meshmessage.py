from collections import deque
def reconstruct_path(how_we_reached_node, start_node, end_node):
    shortest_path = []

    current_node = end_node

    while current_node:
        shortest_path.append(current_node)
        current_node = how_we_reached_node[current_node]

    shortest_path.reverse()
    return shortest_path

def bfs(graph, start_node, end_node):
    if start_node not in graph:
        raise Exception('Start node not in graph')
    if end_node not in graph:
        raise Exception('End node not in graph.')

    nodes_to_visit = deque()
    nodes_to_visit.append(start_node)

    how_we_reached_nodes = {start_node: None}

    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.popleft()

        if current_node == end_node:
            return reconstruct_path(how_we_reached_nodes, start_node, end_node)

        for neighbor in graph[current_node]:
            if neighbor not in how_we_reached_nodes:
                nodes_to_visit.append(neighbor)
                how_we_reached_nodes[neighbor] = current_node

    return None

