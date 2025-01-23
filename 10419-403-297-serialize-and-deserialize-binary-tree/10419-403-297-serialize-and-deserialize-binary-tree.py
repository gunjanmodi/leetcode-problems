# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            return f"{node.val},{dfs(node.left)},{dfs(node.right)}" if node else "#"
        return dfs(root)

    def deserialize(self, data) -> TreeNode:
        nodes = data.split(',')
        nodes.reverse()
        def dfs():
            val = nodes.pop()
            if val != "#":
                node = TreeNode(int(val))
                node.left = dfs()
                node.right = dfs()
                return node
        return dfs()


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))