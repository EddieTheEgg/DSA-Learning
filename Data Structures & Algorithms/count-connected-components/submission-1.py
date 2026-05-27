class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        #We can union find, where we try to union nodes together group

        #The max connect components in a graph can be n nodes at first
        parent = []
        for number in range(n):
            parent.append(number)
        rank = [1] * n

        # parent[1] == 2 and 2 !== 1
        # parent[1] = 
        def findRoot(node):
            if parent[node] != node:
                parent[node] = findRoot(parent[node])
            return parent[node]
        
        def union(nodeA, nodeB):
            rootNodeA = findRoot(nodeA)
            rootNodeB = findRoot(nodeB)
            #The nodes are already unionized because they share the same root node
            if rootNodeA == rootNodeB:
                return False

            #Perform the union by weight
            if rank[rootNodeA] > rank[rootNodeB]:
                parent[rootNodeB] = rootNodeA
                rank[rootNodeA] += rank[rootNodeB]
            else:
                parent[rootNodeA] = rootNodeB
                rank[rootNodeB] += rank[rootNodeA]
            
            return True

        for nodeA, nodeB in edges:
            union(nodeA, nodeB)

        #after we union, our parent array holds the parent of each node
        result = set()
        for i in range(n):
            result.add(findRoot(i))



        return len(result)