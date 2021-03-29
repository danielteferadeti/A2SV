# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: TreeNode, targetSum: int) -> bool:
        if root == None:
            return False
        targetSum -= root.val
        if root.left == None and root.right == None:
            return targetSum == 0

        return self.dfs(root.left, targetSum) or self.dfs(root.right, targetSum)

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.dfs(root, targetSum)
