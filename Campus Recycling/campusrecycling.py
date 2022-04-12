# A class to store a graph edge
class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight
 
 
# A class to store adjacency list nodes
class Node:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
 
 
# A class to represent a graph object
class Graph:
    # Constructor to construct a graph
    def __init__(self, edges, N):
 
        # A list of lists to represent an adjacency list
        self.adj = [None] * N
 
        # allocate memory for the adjacency list
        for i in range(N):
            self.adj[i] = []
 
        # add edges to the undirected graph
        for e in edges:
            # allocate node in adjacency list from src to dest
            node = Node(e.dest, e.weight)
            self.adj[e.src].append(node)
 
 
# Function to print adjacency list representation of a graph
def printGraph(graph):
    for src in range(len(graph.adj)):
        # print current vertex and all its neighboring vertices
        for edge in graph.adj[src]:
            print(f"({src} —> {edge.value}, {edge.weight}) ", end='')
        print()

def dfs_non_recursive(graph, source):

       if source is None or source not in graph:

           return "Invalid input"

       path = []

       stack = [source]

       while(len(stack) != 0):

           s = stack.pop()

           if s not in path:

               path.append(s)

           if s not in graph:

               #leaf node
               continue

           for neighbor in graph[s]:

               stack.append(neighbor)

       return " ".join(path)

if __name__ == '__main__':
 
    # Input: Edges in a weighted digraph (as per the above diagram)
    # Edge `(x, y, w)` represents an edge from `x` to `y` having weight `w`
    #edges = [Edge(0, 1, 6), Edge(1, 2, 7), Edge(2, 0, 5), Edge(2, 1, 4),
            #Edge(3, 2, 10), Edge(4, 5, 1), Edge(5, 4, 3)]

    # Each unit of weight is roughly 250 ft
    edges = [Edge("Early Childhood Education Center", "College of Business", 2),
             Edge("College of Business", "Tech Pointe", 2),
             Edge("College of Business", "IESB", 2),
             Edge("College of Business", "Prescott Library/Wyly Tower", 3),
             Edge("College of Business", "University Hall", 2),
             Edge("University Hall", "Keeny Hall", 1),
             Edge("Keeny Hall", "Bogard Hall", 1),
             Edge("Prescott Library/Wyly Tower", "GTM Hall", 2),
             Edge("GTM Hall", "Hale Hall", 3)]
             
 
    # Input: No of vertices
    N = 6
 
    # construct a graph from a given list of edges
    graph = Graph(edges, N)

    graph2 = {"A":["D","C","B"],
   "B":["E"],
   "C":["G","F"],
   "D":["H"],
   "E":["I"],
   "F":["J"]}
    
    # print adjacency list representation of the graph
    printGraph(graph)

    DFS_path = dfs_non_recursive(graph2, "A")

    print(DFS_path)
    
    
