from asyncore import read
from init import getGraph
from remove_check import isConnected
import sys

 # n is cut vertex if 
    # 1. n is root and it has at least two childer
    # 2. n is not root and it has a child v such that no vertex in subtree of 
    #    v is connected to ancestor of v using backedge
# time of the earliest node that can be reached from subtree of n 
# lowTime[n] = min(disc[n], disc[w], lowTime[v]), w - all back edges visited from u, low[v] - for all children of n 
    # if disc[u] <= low[v] then u is cut vertex
class Graph:
    def __init__(self, graph, nodes):
        self.graph = graph
        self.nodes = nodes
        self.time = 0

    def apAlgo(self):
       
        result = {}
        visited = {}
        discoveredTime = {}
        lowTime = {}  
        
        parent = {}
        time = 0
        for n in self.nodes:
            parent[n] = None
            lowTime[n] = 0
            discoveredTime[n] = 0
            visited[n] = False

                    
        self.dfs(self.nodes[0], result, visited,discoveredTime, lowTime, parent)

        resArr = []
        for k in result:
            resArr.append(k)
        return resArr

    
    def dfs(self, node, result, visited, discoveredTime, lowTime, parent):
        visited[node] = True 
        lowTime[node] = self.time
        discoveredTime[node] = self.time
        self.time = self.time + 1
        childCount = 0

        for child in self.graph[node]:
            if child in visited and visited[child] == False:
                childCount += 1
                parent[child] = node
                self.dfs(child, result, visited, discoveredTime, lowTime, parent)
                lowTime[node] = min(lowTime[node], lowTime[child])
                if parent[node] == None and childCount > 1:
                    result[node] = True
                if parent[node] != None and lowTime[child] >= discoveredTime[node]:
                    result[node] = True
            elif child != parent[node]:
                lowTime[node] = min(lowTime[node], discoveredTime[child])




def main(filename):
    sys.setrecursionlimit(10000000)
    input = getGraph(filename)
    g = Graph(input['graph'], input['nodes'])
    res = g.apAlgo()
    return res
	#print(res)


