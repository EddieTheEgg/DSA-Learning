
import heapq
class MedianFinder:

    #The approach to medain finder with two heaps is thinking of what a median is
    # a median is the middle of a sorted array, meaning 
    # having a minHeap and a maxHeap on the boundaries of the median is the best way
    # the self.small uses maxHeap, because we want the highest value before the median
    # and the self.small uses minHeap, the opposite.
    # THe reason why this works to be the median is because we balance out our heaps
    # we add values in sorted way to the minHeap and maxHeap where when we fetch their root
    # we get the median boundaries because we distributed the values evenly between the two heaps.

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:

        #First check which heap we can add to, usually fallback to small heap if large heap is not possible
        if (self.large and num > self.large[0]):
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        
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
          
        