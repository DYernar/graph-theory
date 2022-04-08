from init import getGraph
import random

def tarjansAlgorithm(graph, nodes):

	def dfs(n, visited):
		if n not in visited:
			visited[n] = True
			stk = [n]
			while (len(stk)):
				s = stk.pop()
				for neighbor in graph[s]:
					if neighbor not in visited:
						visited[neighbor] = True
						stk.append(neighbor)
			return 1
		return 0	
	 
	res = []
	for n in nodes:
		visited = {}
		visited[n] = True
		childsCount = 0
		for neighbor in graph[n]:
			count = dfs(neighbor, visited)
			childsCount += count
		if childsCount > 1:
			res.append(n)

	return res

def main(filename):
	input = getGraph(filename)
	res = tarjansAlgorithm(input['graph'], input['nodes'])
	return res
	#print(res)


