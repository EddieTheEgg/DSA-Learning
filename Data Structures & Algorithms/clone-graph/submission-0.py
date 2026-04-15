"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    
        if not node:
            return None
        
        adjList = {}
        adjList[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in adjList:
                    adjList[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                adjList[cur].neighbors.append(adjList[neighbor])


        return adjList[node]