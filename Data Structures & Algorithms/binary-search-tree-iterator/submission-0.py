# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.cur = root
        self.stack = []

    def next(self) -> int:
        # Keep going left until we reach the end end of left subtree
        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left

        node = self.stack.pop()
        self.cur = node.right #Before going back to root, check nodes if existing on te right satisfying rules
        return node.val

    def hasNext(self) -> bool:
        return bool(self.cur) or bool(self.stack)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()