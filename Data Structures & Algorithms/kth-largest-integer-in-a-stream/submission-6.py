class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [0]  # dummy for 1-based indexing
        for num in nums:
            self.push(num)
            if len(self.heap) - 1 > self.k:
                self.pop()

    def add(self, val: int) -> int:
        if len(self.heap) - 1 < self.k:
            self.push(val)
        elif val > self.heap[1]:
            self.pop()
            self.push(val)
        # else val <= kth largest, do nothing

        return self.heap[1]

    def push(self, val: int):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def pop(self) -> int:
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()

        i = 1
        while 2 * i < len(self.heap):
            if 2 * i + 1 < len(self.heap) and self.heap[i] > self.heap[2 * i + 1] and self.heap[i * 2] > self.heap[i* 2 + 1]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[i * 2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res    
