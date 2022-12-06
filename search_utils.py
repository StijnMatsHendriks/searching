def load_graph(datafile):
    graph = [line.strip('\n').split(" ") for line in open(datafile).readlines()]
    graph = [[int(char) for char in line] for line in graph]
    return graph

def find_neighbours(graph, node, radius, diag=True):
    y, x = node

    neighbours = []
    for i in range(y-radius, y+radius+1):
        for j in range(x-radius, x+radius+1):
            if i >= 0 and i < len(graph) and j >= 0 and j < len(graph):
                neighbours.append((i, j))

    pops = []
    if not diag:
        pops = [neighbour for neighbour in neighbours if neighbour[0] != y and neighbour [1] != x]

    pops.append((y, x))
    neighbours = [neighbour for neighbour in neighbours if neighbour not in pops]

    return neighbours