class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Max Heap

        maxHeap = [-n for n in nums]

        heapq.heapify(maxHeap)

        kth_largest = None
        for _ in range(k):
            kth_largest = heapq.heappop(maxHeap)

        return -kth_largest