package main

import "fmt"

func findOrder(numNodes int, edges [][]int) []int {
	graph := buildGraph(numNodes, edges)

	indegree := map[int]int{}
	for i := 0; i < numNodes; i++ {
		indegree[i] = 0
	}

	for _, neighbors := range graph {
		for _, neighbor := range neighbors {
			indegree[neighbor] += 1
		}
	}

	sources := []int{}
	for node, value := range indegree {
		if value == 0 {
			sources = append(sources, node)
		}
	}

	order := []int{}
	for len(sources) > 0 {
		fmt.Println("indegree", indegree)
		fmt.Println("sources", sources)
		fmt.Println("order", order)
		fmt.Println()
		currentNode := sources[0]
		sources = sources[1:]
		order = append(order, currentNode)

		for _, neighbor := range graph[currentNode] {
			indegree[neighbor] -= 1
			if indegree[neighbor] == 0 {
				sources = append(sources, neighbor)
			}
		}
	}

	if len(order) == numNodes {
		return order
	}

	return []int{}
}

func buildGraph(numNodes int, edges [][]int) map[int][]int {
	graph := map[int][]int{}
	for i := 0; i < numNodes; i++ {
		graph[i] = []int{}
	}

	for _, edge := range edges {
		a, b := edge[0], edge[1]
		graph[a] = append(graph[a], b)
	}

	return graph
}

func main() {
	numNodes := 5
	edges := [][]int{
		{0, 1},
		{0, 2},
		{0, 4},
		{1, 3},
		{1, 4},
		{2, 3},
		{2, 4},
		{3, 4},
	}
	fmt.Println("topological sort", findOrder(numNodes, edges))
}

/*
output:
indegree map[0:0 1:1 2:1 3:2 4:4]
sources [0]
order []

indegree map[0:0 1:0 2:0 3:2 4:3]
sources [1 2]
order [0]

indegree map[0:0 1:0 2:0 3:1 4:2]
sources [2]
order [0 1]

indegree map[0:0 1:0 2:0 3:0 4:1]
sources [3]
order [0 1 2]

indegree map[0:0 1:0 2:0 3:0 4:0]
sources [4]
order [0 1 2 3]

topological sort [0 1 2 3 4]
*/
