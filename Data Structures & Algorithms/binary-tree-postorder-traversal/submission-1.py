# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        visited = [False]
        result = []

        #Main thing to note is that we need a visited array to keep track of when
        #we already traveresd a node. If we alreayd traveresd/vistied then we return
        #else we first check its children before printing/doing anyting with the value
        while stack :
            curr = stack.pop()
            is_visited = visited.pop()
            
            if curr:
                if is_visited:
                    result.append(curr.val)
                else:
                    stack.append(curr)
                    visited.append(True)
                    stack.append(curr.right)
                    visited.append(False)
                    stack.append(curr.left)
                    visited.append(False)
        
        return result
