# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queque = [root]
        average = []
        value_of_nodes = 0
        amount_of_nodes = 0
        while queque:
            for _ in range(len(queque)):
                node = queque.pop(0)
                if node.left:
                    queque.append(node.left)
                if node.right:
                    queque.append(node.right)
                amount_of_nodes += 1
                value_of_nodes += node.val
            average.append(value_of_nodes / amount_of_nodes)
            amount_of_nodes = 0
            value_of_nodes = 0
        return average
