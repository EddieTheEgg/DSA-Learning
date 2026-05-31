class Node:
    def __init__(self, total, L, R):
        self.sum = total
        self.leftChild = None
        self.rightChild = None
        self.L = L #Represnts the node min range
        self.R = R #Reprsents the node max range


class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums)-1) #We need to build the segment tree

    def build(self, nums, L, R):
        if L == R:
            return Node(nums[L], L, R)
        
        M = (L + R) // 2 # Let's say we started with (0,5) medium would be the floor at 2
        root = Node(0, L, R) #Build the segment tree root at first
        root.leftChild = self.build(nums, L, M) # (0, 2)
        root.rightChild = self.build(nums, M+1, R) # (3, 5)

        #After we get the value sof the child nodes, we add those child nodes total together to get root total
        root.sum = root.leftChild.sum + root.rightChild.sum

        return root
    
    def update(self, index: int, val: int) -> None:
        self.updateHelper(self.root, index, val)

    def updateHelper(self, node, index, val) -> None:
        if node.L == index and node.R == index:
           node.sum = val
           return

        M = (node.L + node.R) // 2
        if index > M:
            self.updateHelper(node.rightChild, index, val)
        else:
            self.updateHelper(node.leftChild, index, val)
        node.sum = node.leftChild.sum + node.rightChild.sum

    #Returns the sum between a given range in O(logn) time
    def query(self, L: int, R: int) -> int:
        return self.queryHelper(self.root, L, R)

    def queryHelper(self, node, L, R) -> int:
        #Base Case ~ L and R matches the node L and R
        if node.L == L and node.R == R:
            return node.sum
        
        M = (node.L + node.R) // 2
        if L > M:
            return self.queryHelper(node.rightChild, L, R)
        elif R <= M:
            return self.queryHelper(node.leftChild, L, R)
        else: #The case where the range overlaps the middle
            return self.queryHelper(node.leftChild, L, M) + self.queryHelper(node.rightChild, M+1, R)
