class Node:
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        # Initialize with dummy head and tail nodes
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        node = Node(value)
        # Get the current last node
        prevLastNode = self.tail.prev

        # Insert new node between prevLastNode and tail
        prevLastNode.next = node
        node.prev = prevLastNode
        node.next = self.tail
        self.tail.prev = node

    def appendleft(self, value: int) -> None:
        node = Node(value)
        # Get the current first node
        prevFirstNode = self.head.next

        # Insert new node between head and prevFirstNode
        node.next = prevFirstNode
        prevFirstNode.prev = node
        node.prev = self.head
        self.head.next = node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            # Get the value of the last node
            removedNode = self.tail.prev
            removedVal = removedNode.val
            
            # Update pointers to remove the last node
            newLastNode = removedNode.prev
            newLastNode.next = self.tail
            self.tail.prev = newLastNode

            return removedVal

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            # Get the value of the first node
            removedNode = self.head.next
            removedVal = removedNode.val
            
            # Update pointers to remove the first node
            newFirstNode = removedNode.next
            self.head.next = newFirstNode
            newFirstNode.prev = self.head

            return removedVal