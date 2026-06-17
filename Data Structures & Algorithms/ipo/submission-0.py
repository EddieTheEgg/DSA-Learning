import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        #maxHeap to store the profits of all projects we can currentl yafford
        #minHeap to store all projects by capital, where we want the minimal cost/capital needed at root


        #Where it is sorted by capital, greatest capital at root

        #Step 1, build a min-heap of all projects ordered by capital requirement lowest to highest cost
        maxProfit = []
        minCapital = []
        for (c,p) in zip(capital, profits):
            minCapital.append((c,p))
        heapq.heapify(minCapital)


        for _ in range(k):
            #While there are still projects not worked on, and our total w capital is >= next minCapital (root)
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -p)

            if not maxProfit:
                break

            w += -heapq.heappop(maxProfit)

        return w