class Node:

    def __init__(self, start, end):
        self.leftChild = None
        self.rightChild = None
        self.start = start #the Start time
        self.end = end # The end time
        self.isBooked = False


class MyCalendar:

    #SO we can implement this using segement tree
    #If like the startTime and endTime overlap the middle of a node range that
    # means they end up in two child nodes which is a double book

    #But technically this is fine for the most part, only actually deep down
    #If any of the child nodes have an event already and our current startTime and endTime
    # overlaps then we have an issue an immediate return false, otherwise we keep oging
    # until our startTime and endTime are reached


    
    def __init__(self):
        self.root = Node(0, 1_000_000_000)
        

    def book(self, startTime: int, endTime: int) -> bool:
        # Check first if the node exists and is booked — don't mutate anything
        if not self.query(self.root, startTime, endTime):
            return False
        # Only book if the check passed cleanly
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
            return self.query(node.leftChild, startTime, endTime)   # entirely in left
        elif startTime >= mid:
            return self.query(node.rightChild, startTime, endTime)  # entirely in right
        else:
            return (self.query(node.leftChild, startTime, mid) and  # overlap between both child node, make a seperation
                    self.query(node.rightChild, mid, endTime))

        return True

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

        if startTime < mid:
            self.insert(node.leftChild, startTime, min(endTime, mid))
        if endTime > mid:
            self.insert(node.rightChild, max(startTime, mid), endTime)
            
        if node.leftChild.isBooked and node.rightChild.isBooked:
            node.isBooked = True