from cmath import inf
import networkx as nx
import matplotlib.pyplot as plt
import sys

def getGraph(filename) :
	graph = {}
	G = nx.Graph()

	file = open(filename, 'r')
	lines = file.readlines()
	file.close()
	n, *lines = lines
	for line in lines:
		first = line.rstrip().split()[0] 
		second = line.rstrip().split()[1] 
		if first not in graph:
			graph[first] = []
		if second not in graph:
			graph[second] = []
		G.add_edge(first, second)
		G.add_nodes_from([first, second])
		graph[first].append(second)
		graph[second].append(first)

	# nx.draw_networkx(G)
	# plt.show()
	return {'graph':graph, 'nodes': list(G.nodes())}

