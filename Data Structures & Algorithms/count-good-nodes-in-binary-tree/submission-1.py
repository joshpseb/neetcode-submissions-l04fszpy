# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0
        def dfs(node, maxVal):
            if not node:
                return
            if node.val >= maxVal:
                nonlocal total
                total += 1
                maxVal = node.val
            dfs(node.right, maxVal)
            dfs(node.left, maxVal)
        dfs(root, root.val)
        return total