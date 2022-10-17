from collections import deque
class Solution(object):
    def findOrder(self, numNodes, edges):
        """
        :type numNodes: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = self.buildGraph(numNodes, edges)
        indegree = {x:0 for x in range(numNodes)}
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                indegree[neighbor] += 1
        
        sources = deque()
        for node, value in indegree.items():
            if value == 0:
                sources.append(node)
                
        order = []
        while len(sources) > 0:
            print("indegree", indegree)
            print("sources", sources)
            print("order", order)
            print("")
            currentNode = sources.popleft()
            order.append(currentNode)
            
            for neighbor in graph[currentNode]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    sources.append(neighbor)
        
        if len(order) == numNodes:
            return order
        
        return []
            
    
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

''' 
outout:
('indegree', {0: 0, 1: 1, 2: 1, 3: 2, 4: 4})
('sources', deque([0]))
('order', [])

('indegree', {0: 0, 1: 0, 2: 0, 3: 2, 4: 3})
('sources', deque([1, 2]))
('order', [0])

('indegree', {0: 0, 1: 0, 2: 0, 3: 1, 4: 2})
('sources', deque([2]))
('order', [0, 1])

('indegree', {0: 0, 1: 0, 2: 0, 3: 0, 4: 1})
('sources', deque([3]))
('order', [0, 1, 2])

('indegree', {0: 0, 1: 0, 2: 0, 3: 0, 4: 0})
('sources', deque([4]))
('order', [0, 1, 2, 3])

('topological sort', [0, 1, 2, 3, 4])
'''