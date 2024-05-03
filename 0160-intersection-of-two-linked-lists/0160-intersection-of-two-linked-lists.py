# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m, n = 0, 0
        node1, node2 = headA, headB
        while node1:
            m += 1
            node1 = node1.next
        
        while node2:
            n += 1
            node2 = node2.next
        
        diff = abs(m - n)

        node1, node2 = headA, headB
        if m > n:
            for _ in range(diff):
                node1 = node1.next
        else:
            for _ in range(diff):
                node2 = node2.next

        while node1 and node2:
            if node1 == node2:
                return node1
            node1 = node1.next
            node2 = node2.next

        


        