import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        #Sort capital by minHeap

        #Then sort valid project profits by maxHeap

        possibleProfits = []
        capitalProjects = []

        #Build a sorted array of available projects from least to most capital
        #We get access to larger capital projects by working on the samller ones first hence minHeap
        for (c, p) in zip(capital, profits):
            heapq.heappush(capitalProjects, (c,p))
        
        for _ in range(k):
            #For every project, we want to choose the minimal capital project that gives us max profit
            #First at our given w capital, see what available projects we can use
            while capitalProjects and capitalProjects[0][0] <= w:
                c, p = heapq.heappop(capitalProjects)
                heapq.heappush(possibleProfits, -p)
            
            #Afte rgetting all avaialbe projects, our possibelProfits
            # sort the avaialbe projects our capital w can take on and the max profit
            # is at the root of possibleProfits since it is maxHeap
            # But if there is no maxHeap or projects early exit
            if not possibleProfits:
                break
            
            # Fetch the max profit in the maxHeap of available projects
            w += -1 * heapq.heappop(possibleProfits)
        
        return w
