# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        data = [k, 0]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            data[0] -= 1
            if data[0] == 0:
                data[1] = node.val
                return
            dfs(node.right)

        dfs(root)
        return data[1]
        