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
        #Makes a copy of the original node and assign it to the adjList with an empty array of neighbors (those need to be copied as well eventually)
        adjList[node] = Node(node.val) # so currently adjList = { original node : copy of original node (with neighbors[]) }
        q = deque()
        q.append(node) #add original node so we can copy its neighbors and populate the copied nodes.


        while q:
            curNode = q.popleft()
            for neighbor in curNode.neighbors:
                if neighbor not in adjList:
                    adjList[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                #The curNode's copied node remember has an empty neighbor array, so we populate with the copied neighbor, which is a node that could point to other nodes etc.
                adjList[curNode].neighbors.append(adjList[neighbor])
        
        return adjList[node]
