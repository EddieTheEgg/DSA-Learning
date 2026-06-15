
import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        #First check if all nums in in the small valued heap is less than large valued heap
        if (self.small and self.large and -1 * self.small[0] > self.large[0]):
            poppedValue = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, poppedValue)
        
        #We now know all values in small heap are smaller than large heap
        #We need to check if their heap sizes are at max difference one now
        if (len(self.small) > len(self.large) + 1):
            poppedValue = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, poppedValue)
        if (len(self.large) > len(self.small) + 1):
            poppedValue = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * poppedValue)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        
        return (-1 * self.small[0] + self.large[0]) / 2
          
        