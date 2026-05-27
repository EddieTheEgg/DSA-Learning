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

        #After we union, not every node is path compressed fully
        # for eaxmple [0,1], [1,2], [3,4] the parent of 0 is 1
        # and the parent of 1 is 2. When we do union [1,2] we don't set
        #parent of 0 to be 2 as well. This is a path compression gap hence
        # why we can't just set(parent) and return length like that.
        result = set()
        for i in range(n):
            result.add(findRoot(i))



        return len(result)