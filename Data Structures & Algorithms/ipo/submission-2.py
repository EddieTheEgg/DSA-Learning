import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        #maxHeap to store the profits of all projects we can currentl yafford
        #minHeap to store all projects by capital, where we want the minimal cost/capital needed at root


        #Where it is sorted by capital, greatest capital at root

        #Step 1, build a min-heap of all projects ordered by capital requirement lowest to highest cost
        maxProfit = []
        minCapital = []
        #Add all projects to minCapital as a minHeap so we can find projects sorted from minimal cost to most expensive capital
        for (c,p) in zip(capital, profits):
            minCapital.append((c,p))
        heapq.heapify(minCapital)

        #We can only work on max amount of projects (k), so this is overarching loop
        for _ in range(k):
            # We will try to work on as many projects as possible by popping and moving it to maxProfit
            # as long as the project's capital is less than our total current capital
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p) #When adding the project we can work on to maxProfit, we want to sort by maxHeap, the maximal capital we can gain at root

            #This only happens if our 
            if not maxProfit:
                break

            #After we filtered out all available projects from minHeap minCapital, and moved it to possible project
            # to work on in maxHeap maxProfit, we can pop the root of maxHeap to get the max profit which adds to our capital
            w += -heapq.heappop(maxProfit)

        return w