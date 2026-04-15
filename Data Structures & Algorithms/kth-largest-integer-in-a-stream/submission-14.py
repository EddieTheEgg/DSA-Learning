class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [0]  
        for num in nums: #Convert the array into a heap structure
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.heap) - 1 < self.k: #If there are less than k integers than kth integer, we need to add the value
            self.push(val)
        elif val > self.heap[1]: #We have the 
            self.push(val)
            self.pop()
           

        return self.heap[1]

    #Heap helper to push a value into a heap structure
    def push(self, val: int):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i> 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2

    #Heap helper to remove a value from a heap structure
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
