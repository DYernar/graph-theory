

from pickle import TRUE
from init import getGraph
import copy


# complexity: O(V(V*E)) 
def removeAndCheck(graph, nodes):
    if not isConnected(graph, len(nodes)):
        print("invalid input.txt file. graph should be connected")
        return []

    res = []
    for n in nodes:
        gCopy = copy.deepcopy(graph)
        #remove the node
        del gCopy[n]
        #remove edges
        for k  in gCopy:
            if n in gCopy[k]:
                gCopy[k].remove(n)
        if not isConnected(gCopy, len(nodes) - 1):
            res.append(n)
    return res


def isConnected(graph, size):
    queue = []
    for key in graph:
        queue.append(key)
        break
    visited = {}
    while queue:
        current = queue[0]
        queue.pop(0)
        if current in visited:
            continue
        visited[current] = True
        neighbors = graph[current]
        for n in neighbors:
            if n not in visited:
                queue.append(n)
    return len(visited) == size


def main(filename):
	input = getGraph(filename)
	res = removeAndCheck(input['graph'], input['nodes'])
	return res
	#print(res)
