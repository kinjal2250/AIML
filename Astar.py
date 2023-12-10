import heapq

# Define the graph as an adjacency list
graph = {
    'S': {'A': 1, 'G': 12},
    'A': {'S': 1, 'C': 1, 'B': 3},
    'B': {'A': 3, 'D': 3},
    'C': {'A': 1, 'D': 1, 'G': 2},
    'D': {'B': 3, 'C': 1, 'G':3},
    'G': {'S': 12, 'D': 3, 'C': 2},
}

# Input heuristic values (h(n)) for each node
heuristics = {}
for node in graph.keys():
    heuristic_value = int(input(f"Enter heuristic value (h(n)) for node {node}: "))
    heuristics[node] = heuristic_value

# A* algorithm
def astar(graph, start, goal, heuristics):
    open_list = [(0, start)]
    g_scores = {node: float('inf') for node in graph}
    g_scores[start] = 0
    came_from = {}

    while open_list:
        current_g, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.insert(0, current_node)
                current_node = came_from[current_node]
            path.insert(0, start)
            return path, g_scores[goal]

        for neighbor, cost in graph[current_node].items():
            tentative_g = g_scores[current_node] + cost
            if tentative_g < g_scores[neighbor]:
                came_from[neighbor] = current_node
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristics[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))

    return None, None

start_node = input("Enter the start node: ").upper()
goal_node = input("Enter the goal node: ").upper()

if start_node in graph and goal_node in graph:
    path, total_cost = astar(graph, start_node, goal_node, heuristics)
    if path:
        print("Shortest path:", " -> ".join(path))
        print("Total cost:", total_cost)
    else:
        print("No path found.")
else:
    print("Invalid node names. Please use alphabetic nodes")


# Import the heapq module to use a priority queue (min-heap) for efficiently managing nodes to be explored.

# Define the graph as an adjacency list. It represents a set of nodes ('S', 'A', 'B', 'C', 'D', 'G') and their connections with associated edge costs.

# Input heuristic values (h(n)) for each node using user input. These heuristic values are used to guide the A* algorithm in estimating the cost to reach the goal from each node.

# Define the A* algorithm in the astar function. This function takes the graph, start node, goal node, and heuristics as input and returns the shortest path and the total cost.

# Initialize the open list with the start node and a priority value of 0. The g_scores dictionary is initialized to hold the cost of getting to each node from the start node, initialized to infinity for all nodes except the start node.

# The came_from dictionary will store the previous node in the shortest path from the start node to the current node.

# The A* algorithm uses a while loop that continues as long as there are nodes to explore in the open_list.

# In each iteration, it pops the node with the lowest priority (lowest total cost) from the open_list.

# If the current node is the goal node, it reconstructs the path by backtracking through the came_from dictionary.

# It then returns the path and the total cost.

# If the current node is not the goal, it examines its neighbors, calculates tentative g_scores, and updates them if a shorter path is found. It also calculates the f_score, which is the sum of the tentative g_score and the heuristic for the neighbor. This f_score is used to prioritize nodes in the open_list.

# If a shorter path is found to a neighbor, the came_from and g_scores dictionaries are updated, and the neighbor is added to the open_list with its f_score.

# If the goal is not reached and there are no more nodes to explore, the function returns None.

# Input the start and goal nodes from the user, ensuring they are valid node names (A-H).

# If the start and goal nodes are valid, call the astar function to find the shortest path.

# If a path is found, print the path and the total cost. If no path is found, print "No path found."