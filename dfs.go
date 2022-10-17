package main

import "fmt"

func findOrder(numNodes int, edges [][]int) []int {
	graph := buildGraph(numNodes, edges)
	visiting := map[int]bool{}
	visited := map[int]bool{}
	order := []int{}
	for node, _ := range graph {
		if dfs(graph, node, visiting, visited, &order) {
			return []int{}
		}
	}

	return order
}

func dfs(graph map[int][]int, node int, visiting map[int]bool, visited map[int]bool, order *[]int) bool {
	fmt.Println("visiting", visiting)
	fmt.Println("visited", visited)
	fmt.Println("order", *order)
	fmt.Println()
	if _, found := visited[node]; found {
		return false
	}

	if _, found := visiting[node]; found {
		return true
	}

	visiting[node] = true
	for _, neighbor := range graph[node] {
		if dfs(graph, neighbor, visiting, visited, order) {
			return true
		}
	}

	*order = append([]int{node}, *order...)
	delete(visiting, node)
	visited[node] = true
	return false
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
visiting map[]
visited map[]
order []

visiting map[0:true]
visited map[]
order []

visiting map[0:true 1:true]
visited map[]
order []

visiting map[0:true 1:true 3:true]
visited map[]
order []

visiting map[0:true 1:true]
visited map[3:true 4:true]
order [3 4]

visiting map[0:true]
visited map[1:true 3:true 4:true]
order [1 3 4]

visiting map[0:true 2:true]
visited map[1:true 3:true 4:true]
order [1 3 4]

visiting map[0:true 2:true]
visited map[1:true 3:true 4:true]
order [1 3 4]

visiting map[0:true]
visited map[1:true 2:true 3:true 4:true]
order [2 1 3 4]

visiting map[]
visited map[0:true 1:true 2:true 3:true 4:true]
order [0 2 1 3 4]

visiting map[]
visited map[0:true 1:true 2:true 3:true 4:true]
order [0 2 1 3 4]

visiting map[]
visited map[0:true 1:true 2:true 3:true 4:true]
order [0 2 1 3 4]

visiting map[]
visited map[0:true 1:true 2:true 3:true 4:true]
order [0 2 1 3 4]
*/
