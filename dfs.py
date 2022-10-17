from collections import deque
class Solution(object):
    def findOrder(self, numNodes, edges):
        """
        :type numNodes: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = self.buildGraph(numNodes, edges)
        visited = set()
        visiting = set()
        order = deque()
        
        for node in graph:
            if self.dfs(graph, node, visited, visiting, order):
                return []
        return list(order)
    
    def dfs(self, graph, node, visited, visiting, order):
        print("visiting", visiting)
        print("visited", visited)
        print("order", order)
        print("")
        if node in visited:
            return False
        if node in visiting:
            return True
        
        visiting.add(node)
        for neighbor in graph[node]:
            if self.dfs(graph, neighbor, visited, visiting, order):
                return True
        order.appendleft(node)
        visiting.remove(node)
        visited.add(node)
        return False
    
    def buildGraph(self, numNodes, edges):
        graph = {x:[] for x in range(numNodes)}
        for edge in edges:
            a, b = edge
            graph[a].append(b)
        
        return graph


if __name__ == "__main__":
    solution = Solution()
    numNodes = 5
    edges = [
        [0, 1],
        [0, 2],
        [0, 4],
        [1, 3],
        [1, 4],
        [2, 3], 
        [2, 4],
        [3, 4],
    ]
    print("topological sort", solution.findOrder(numNodes, edges))


"""
output:
('visiting', set([]))
('visited', set([]))
('order', deque([]))

('visiting', set([0]))
('visited', set([]))
('order', deque([]))

('visiting', set([0, 1]))
('visited', set([]))
('order', deque([]))

('visiting', set([0, 1, 3]))
('visited', set([]))
('order', deque([]))

('visiting', set([0, 1]))
('visited', set([3, 4]))
('order', deque([3, 4]))

('visiting', set([0]))
('visited', set([1, 3, 4]))
('order', deque([1, 3, 4]))

('visiting', set([0, 2]))
('visited', set([1, 3, 4]))
('order', deque([1, 3, 4]))

('visiting', set([0, 2]))
('visited', set([1, 3, 4]))
('order', deque([1, 3, 4]))

('visiting', set([0]))
('visited', set([1, 2, 3, 4]))
('order', deque([2, 1, 3, 4]))

('visiting', set([]))
('visited', set([0, 1, 2, 3, 4]))
('order', deque([0, 2, 1, 3, 4]))

('visiting', set([]))
('visited', set([0, 1, 2, 3, 4]))
('order', deque([0, 2, 1, 3, 4]))

('visiting', set([]))
('visited', set([0, 1, 2, 3, 4]))
('order', deque([0, 2, 1, 3, 4]))

('visiting', set([]))
('visited', set([0, 1, 2, 3, 4]))
('order', deque([0, 2, 1, 3, 4]))

('topological sort', [0, 2, 1, 3, 4])
"""