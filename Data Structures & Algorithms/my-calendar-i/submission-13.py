class Node:
    def __init__(self, start, end):
        self.leftChild = None
        self.rightChild = None
        self.start = start
        self.end = end
        self.isBooked = False

class MyCalendar:
    def __init__(self):
        self.root = Node(0, 1_000_000_000)

    def book(self, startTime: int, endTime: int) -> bool:
        # Check if the startTime to endTime range exist in the segment tree calender
        if not self.query(self.root, startTime, endTime):
            return False
        
        # The startTime to endTime range doesn't exist, we can add/build into the tree that time range.
        self.insert(self.root, startTime, endTime)
        return True

    #Searches for a node and returns True if the node does not exist or False if the node exists and is booked
    def query(self, node, startTime, endTime) -> bool:
        if node is None:
            return True
        if node.isBooked:
            return False
        if startTime >= node.end or endTime <= node.start: # The node does not exist/overlap
            return True
        
        mid = (node.start + node.end) // 2
        
        if endTime <= mid:
            return self.query(node.leftChild, startTime, endTime)
        elif startTime >= mid:
            return self.query(node.rightChild, startTime, endTime)
        else:
            #The scenario the time range overlaps the middle point, we divide the recursive step to sub branches
            return self.query(node.leftChild, startTime, mid) and self.query(node.rightChild, mid, endTime)

    # Usually after a query, if the time range does not exist in the tree we will insert it
    def insert(self, node, startTime, endTime):
        if node.isBooked:
            return
        if node.start == startTime and node.end == endTime:
            node.isBooked = True
            return
        
        mid = (node.start + node.end) // 2
        
        # If either child nodes dont exist, create them before we insert the nodes to them possibly
        if node.leftChild is None:
            node.leftChild = Node(node.start, mid)
        if node.rightChild is None:
            node.rightChild = Node(mid, node.end)
        
        if endTime <= mid: #U may wonder why we include mid, the problem says this is a half-open interval calender meaning endTime is not inclusive
        # So that means if our endTime = mid, we are technically not including it, like an array length of 5 is 0,1,2,3,4. 
        # Think of it like slice [:mid] includes everything but mid itself. so like endTime would not included but all the values before it
            self.insert(node.leftChild, startTime, endTime)
        elif startTime >= mid: #The mid aka startTime can be included on the right child and like slice [mid:] here would include mid and up as intended.
            self.insert(node.rightChild, startTime, endTime)
        else: #This is where overlap of the medium we need to insert in two halves
            self.insert(node.leftChild, startTime, mid)
            self.insert(node.rightChild, mid, endTime)
        
        if node.leftChild.isBooked and node.rightChild.isBooked:
            node.isBooked = True

