# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find Middle
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow
        
        # Reverse from middle
        node, prev = mid.next, None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
            
        mid.next = prev
        
        # Re arrange and disconnect the middle
        p1, p2 = head, mid.next
        mid.next = None

        while p1 and p2:
            p1_next, p2_next = p1.next, p2.next
            p1.next = p2
            p2.next = p1_next
            p1 = p1_next
            p2 = p2_next
