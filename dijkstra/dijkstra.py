from cmath import inf
import networkx as nx
import matplotlib.pyplot as plt

# you may need to install networkx
#### here we are just reading and converting the graph into adjacency matrix

n = -1
graph = {}
G = nx.Graph()

file = open('graph.txt', 'r')
lines = file.readlines()

for line in lines:
    # first line is just number of edges in a graph
    if n == -1:
        n = line
        continue
    vals = line.split(" ")
    first = vals[0]
    second = vals[1]
    weight = vals[2]

    if first not in graph:
        graph[first] = {}
    if second not in graph:
        graph[second] = {}
    G.add_edge(first, second, weight=int(weight))
    graph[first][second] = int(weight)
    graph[second][first] = int(weight)

nx.draw_networkx(G)
plt.show()


################################
### START OF DIJKSTRA ALGORITHM
###############################
def dijkstra(graph, start):
    distances = {} # stores the min cost of reaching the node
    unvisitedNodes = graph # stores not visited nodes

    # set distances to nodes as infinity
    for i in graph:
        distances[i] = float('inf')
    
    # the cost of traveling from start to itself is zero
    distances[start] = 0

    # repeat until we don't visit all the nodes
    while unvisitedNodes:
        # take the unvisited node with lowest distance
        closestNode = None
        for node in unvisitedNodes:
            if closestNode is None or distances[node] < distances[closestNode]:
                closestNode = node

        # get the neighbors of the closestNode
        neighbors = graph[closestNode].items()

        # for each neighbor check if we can reach it with lower cost
        # if so update the distance
        for n, w in neighbors:
            if distances[closestNode] + w < distances[n]:
                distances[n] = distances[closestNode] +w

        # remove visited node
        unvisitedNodes.pop(closestNode)

    return distances

##############################
### END OF DIJKSTRA ALGORITHM
#############################

# ask for inputs
start = input("please insert a starting vertex: ")
distances = dijkstra(graph, start)
goal = input("please insert a goal vertex: ")

res = distances[goal]

if res == inf:
    print("there is no path from {} to {}".format(start, goal))
else:
    print('from {} to {} costs {}'.format(start, goal, res))

  
