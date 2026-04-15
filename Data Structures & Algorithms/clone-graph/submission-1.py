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
        #Add original node to adjList, and assign it a new node with the original value, but an empty array of neighbors
        #This is so as we iterate through the original node's neighbors, we can add it back + go find other nodes
        adjList[node] = Node(node.val)
        q = deque()
        q.append(node)

        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in adjList:
                    adjList[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                adjList[cur].neighbors.append(adjList[neighbor])


        return adjList[node]