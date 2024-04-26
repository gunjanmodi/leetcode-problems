# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s = set()
        node = headA
        while node:
            s.add(node)
            node = node.next

        node = headB
        while node:
            if node in s:
                break
            node = node.next
        return node
        