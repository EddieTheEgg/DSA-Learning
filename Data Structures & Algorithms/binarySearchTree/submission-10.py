class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None



class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if self.root == None:
            self.root = newNode
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left == None:
                    current.left = newNode
                    return
                current = current.left
            elif key > current.key:
                if current.right == None:
                    current.right = newNode
                    return
                current = current.right
            else:
                current.val = val
                return


    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        curr = self.root

        while curr and curr.left:
            curr = curr.left
        return curr.val if curr else -1


    def getMax(self) -> int:
        curr = self.root

        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def findMin(self, node: TreeNode):
        curr = node
        while curr and curr.left:
            curr = curr.left
        return curr

    def removeHelper(self, curr, key) -> TreeNode:
        if curr == None:
            return None
        
        #Searching for the key to remove first
        if curr.key < key:
            curr.right = self.removeHelper(curr.right, key) #deletes by assigning the pointer to the child node (if there is one) of the deleted node
        elif curr.key > key:
            curr.left = self.removeHelper(curr.left, key)
        else: #the case we do find the key, now we will process the remove carefully
            if curr.left == None:
                return curr.right
            elif curr.right == None:
                return curr.left
            else: #Scenario where there are children on left and right subtree
                #Swap curr node with inorder successor
                # We want the value greatest in right sub tree because it is
                # greater than left subtree, but still smaller than rest of the right subtree
                # maintaning the BST structure
                #So, find the min of right subtree
                minNode = self.findMin(curr.right)
                #Perform swap with current to be deleted node
                curr.key = minNode.key
                curr.val = minNode.val
                #Remove the duplicate node we used to swap with recursion
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr



    def getInorderKeys(self) -> List[int]:
        result = []
        self.getInorderKeysHelper(self.root, result)
        return result


    def getInorderKeysHelper(self, root: TreeNode, result: List[int]):
        if root == None:
            return
        
        self.getInorderKeysHelper(root.left, result)
        result.append(root.key)
        self.getInorderKeysHelper(root.right, result)

    

