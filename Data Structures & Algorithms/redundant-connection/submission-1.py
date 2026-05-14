class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        #Index i in parent array represents node i
        # The VALUE at parent[i] is the parent of node i
        # The rank value at each node i represents how many
        # nodes share that parent[i] root node (This is union by size not union by height)
           # Note we can also union by height, which means we
           # can't add the amount of nodes from each rank, but instead
           # when we combine trees of same rank, we just add one layer that's it
           # See the lesson example, but union by size here below is more common
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]

        def union(point1, point2):
            p1 = find(point1)
            p2 = find(point2)

            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]