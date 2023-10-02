# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        result = root.val if root.val in range(low, high + 1) else 0

        if root.val > low:
            result += self.rangeSumBST(root.left, low, high)

        if root.val < high:
            result += self.rangeSumBST(root.right, low, high)

        return result
