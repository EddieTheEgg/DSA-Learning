class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Sort by Educlidean distance
        # Return k closest points
        # So lower the distance, the better, minHeap
        res = []

        heap = [(x**2 + y**2, [x, y]) for x, y in points]

        heapq.heapify(heap)

        i = 0
        while i < k:
            res.append(heapq.heappop(heap)[1])
            i += 1

        return res