class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort by Euclidean distance
        # Return k closest points
        # So lower the distance, the better, minHeap
        res = []
        minHeap = []

        for x, y in points:
            dist = x**2 + y**2 
            minHeap.append((dist, [x, y]))

        heapq.heapify(minHeap)

        i = 0
        while i < k:
            res.append(heapq.heappop(minHeap)[1])
            i += 1

        return res