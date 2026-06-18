import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        #Sort capital by minHeap

        #Then sort valid project profits by maxHeap

        possibleProfits = []
        capitalProjects = []

        for (c, p) in zip(capital, profits):
            heapq.heappush(capitalProjects, (c,p))
        
        for _ in range(k):
            #For every project, we want to choose the minimal capital project that gives us max profit
            #First at our given w capital, see what available projects we can use
            while capitalProjects and capitalProjects[0][0] <= w:
                c, p = heapq.heappop(capitalProjects)
                heapq.heappush(possibleProfits, -p)
            
            if not possibleProfits:
                break
            
            w += -1 * heapq.heappop(possibleProfits)
        
        return w
