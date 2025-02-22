# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(node):
            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
                return -1

            return max(left_depth, right_depth) + 1

        return depth(root) != -1
