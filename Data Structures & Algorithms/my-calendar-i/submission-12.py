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
        if not self.query(self.root, startTime, endTime):
            return False
        self.insert(self.root, startTime, endTime)
        return True

    def query(self, node, startTime, endTime) -> bool:
        if node is None:
            return True
        if node.isBooked:
            return False
        if startTime >= node.end or endTime <= node.start:
            return True
        mid = (node.start + node.end) // 2
        if endTime <= mid:
            return self.query(node.leftChild, startTime, endTime)
        elif startTime >= mid:
            return self.query(node.rightChild, startTime, endTime)
        else:
            return (self.query(node.leftChild, startTime, mid) and
                    self.query(node.rightChild, mid, endTime))

    def insert(self, node, startTime, endTime):
        if node.isBooked:
            return
        if node.start == startTime and node.end == endTime:
            node.isBooked = True
            return
        mid = (node.start + node.end) // 2
        if node.leftChild is None:
            node.leftChild = Node(node.start, mid)
        if node.rightChild is None:
            node.rightChild = Node(mid, node.end)
        if endTime <= mid:
            self.insert(node.leftChild, startTime, endTime)
        elif startTime >= mid:
            self.insert(node.rightChild, startTime, endTime)
        else:
            self.insert(node.leftChild, startTime, mid)
            self.insert(node.rightChild, mid, endTime)
        if node.leftChild.isBooked and node.rightChild.isBooked:
            node.isBooked = True