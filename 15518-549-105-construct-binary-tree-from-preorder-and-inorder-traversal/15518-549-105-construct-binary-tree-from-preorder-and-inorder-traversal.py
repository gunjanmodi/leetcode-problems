# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        value_idx_map = {v: i for i, v in enumerate(inorder)}
        preorder_queue = collections.deque(preorder)
        n = len(inorder) - 1
        def dfs(i, j):
            if i > j:
                return
            node = TreeNode(preorder_queue.popleft())
            k = value_idx_map[node.val]
            node.left = dfs(i,k-1)
            node.right = dfs(k+1, j)
            return node

        return dfs(0, len(inorder) - 1)
