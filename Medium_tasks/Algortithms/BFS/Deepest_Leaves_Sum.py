class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level = [root]
        while level and root:
            next_level, level_sum = [], 0

            for node in level:
                level_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            level = next_level
        return level_sum