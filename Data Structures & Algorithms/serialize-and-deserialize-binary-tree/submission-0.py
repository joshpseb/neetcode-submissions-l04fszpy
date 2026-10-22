# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # plan: use BFS, insert in order, if no child insert None
        out = []

        #bfs
        q = deque([root])
        layer = 0
        while q:
            node = q.popleft()
            if node:
                out.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                out.append("N")
                #q.append(None)
            
        return ",".join(out)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        
        if vals[0] == "N":
            return None

        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1

        while q:
            node = q.popleft()
            if vals[i] == "N":
                node.left = None
            else:
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if vals[i] == "N":
                node.right = None
            else:
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root

                










