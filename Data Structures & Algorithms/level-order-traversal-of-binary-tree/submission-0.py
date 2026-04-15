# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque() #initiate a queue list

        if root: #if the tree exist, 
            queue.append(root)

        while len(queue) > 0:
            miniArr = []
            for i in range(len(queue)):
                curr = queue.popleft()
                miniArr.append(curr.val)
                if curr.left: 
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            result.append(miniArr)
        
        return result

