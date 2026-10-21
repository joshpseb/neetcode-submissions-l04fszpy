# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: #neet
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, leftBoundary, rightBoundary):
            if not node:
                return True
            if not (node.val < rightBoundary and node.val > leftBoundary):
                return False

            return (dfs(node.left, leftBoundary, node.val) 
                    and dfs(node.right, node.val, rightBoundary))


        
        return dfs(root, -float('inf'), float('inf'))