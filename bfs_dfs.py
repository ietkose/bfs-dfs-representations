# adjacency list

print("\nBFS & DFS REPRESENTATIONS\n")
print(
    "Graph:\n"
    "--------------------------\n"
    "         0.\n"        
    "       /    \\\n"
    "      1.  —  2.\n"    
    "     /  \\   /  \n"    
    "    4. —  3. — 5.\n"  
    "    |  \\  |  /\n"   
    "    7.    6.\n"
    "--------------------------\n"
)

numbers =  []
for i in range(0, 8):
    number = input("Enter an integer number (maximum 8 numbers): ")
    numbers.append(number)
print()

graph = {
    numbers[0]: [numbers[1], numbers[2]],
    numbers[1]: [numbers[0], numbers[2], numbers[3], numbers[4]],
    numbers[2]: [numbers[0], numbers[1], numbers[3]],
    numbers[3]: [numbers[1], numbers[2], numbers[4], numbers[5], numbers[6]],
    numbers[4]: [numbers[1], numbers[3], numbers[6], numbers[7]],
    numbers[5]: [numbers[3], numbers[6]],
    numbers[6]: [numbers[3], numbers[4], numbers[5]],
    numbers[7]: [numbers[4]]
}

# BREADTH-FIRST SEARCH (BFS)
def bfs(graph, start_node):
    visited = [] 
    queue = [start_node] 

    while queue:
        node = queue.pop(0) # pop starts the queue from the beginning
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited

# DEPTH-FIRST SEARCH (DFS)
def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = []
    
    if start_node not in visited:
        visited.append(start_node)
        for neighbor in graph[start_node]:
            dfs(graph, neighbor, visited)
    
    return visited

if __name__ == "__main__":
    start_node = numbers[0]
    
    print("*" * 37)
    print(f"Start Node: {start_node}")
    print("-" * 37)

    bfs_result = bfs(graph, start_node)
    print("Breadth-First Search (BFS) Result:")
    print(" -> ".join(bfs_result))
    print("-" * 37)

    dfs_result = dfs(graph, start_node)
    print("Depth-First Search (DFS) Result:")
    print(" -> ".join(dfs_result))
    print("*" * 37)
