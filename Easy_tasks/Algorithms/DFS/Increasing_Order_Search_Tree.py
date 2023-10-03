# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return None

            dfs(node.left)

            self.prev.right = node
            node.left = None
            self.prev = node

            dfs(node.right)

        self.prev = TreeNode()
        self.root = self.prev
        dfs(root)

        return self.root.right
