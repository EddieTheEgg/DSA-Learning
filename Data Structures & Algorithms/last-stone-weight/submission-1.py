class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)

        # 0  1  2  3
        # 0 36 15 20
        while len(max_heap) > 1:
            stone_x = -heapq.heappop(max_heap)
            stone_y = -heapq.heappop(max_heap)

            if stone_x != stone_y:
                heapq.heappush(max_heap, stone_y - stone_x)

        return -max_heap[0] if max_heap else 0
            