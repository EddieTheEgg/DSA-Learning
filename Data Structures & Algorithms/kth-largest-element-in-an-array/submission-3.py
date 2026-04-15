class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Max Heap

        maxHeap = [-n for n in nums]

        heapq.heapify(maxHeap)

        i = 0
        while i < k-1:
            heapq.heappop(maxHeap)
            i += 1

        return -maxHeap[0]