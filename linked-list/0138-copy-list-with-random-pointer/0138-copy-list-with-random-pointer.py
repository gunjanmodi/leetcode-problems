"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        new_head = ListNode(-1)
        node, running_node = head, new_head
        
        while node:
            if node not in d:
                d[node] = Node(node.val)
                
            if node.random:
                if node.random not in d:
                    d[node.random] = Node(node.random.val)
                d[node].random = d[node.random]
                
            running_node.next = d[node]
            
            node = node.next
            running_node = running_node.next
            
        return new_head.next
        