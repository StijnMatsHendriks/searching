from search_utils import load_graph, find_neighbours
  
def BFS(graph, start_node, end_node=None):
    Q = [start_node]
    visited = {}
    visited[start_node] = [start_node, 0]

    while Q:
        from_node = Q.pop()
        to_nodes = find_neighbours(graph, from_node, radius=1, diag=False)
        to_nodes = [to_node for to_node in to_nodes if to_node not in visited.keys()]

        for to_node in to_nodes:
            visited[to_node] = [from_node, visited[from_node][1] + 1]
            
            # Check if we are there
            if end_node and end_node in visited.keys():
                return visited
            
            # Otherwise, continue    
            Q.insert(0, to_node)
        
    return visited


def backwards_traversal(visited, start_node, end_node):
    backward_path = []
    Q = [end_node]
    total_cost = visited[end_node][1]

    while start_node not in backward_path:
        node = Q.pop()
        backward_path.append(node)
        Q.insert(0, visited[node][0])

    forward_path = backward_path[::-1]
    return forward_path, total_cost
        

if __name__ == "__main__":
    graph = load_graph('graph.txt')
    start_node = (1,1)
    end_node = (3,4)
    visited = BFS(graph, start_node, end_node)
    forward_path, total_cost = backwards_traversal(visited, start_node, end_node)
    print(f"The path was: {forward_path} and the cost of this path was: {total_cost}")


    

    