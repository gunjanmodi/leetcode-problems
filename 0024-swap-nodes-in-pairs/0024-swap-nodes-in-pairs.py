# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
   
        if head is None:
            return head
        if head.next is None:
            return head

        new_head = ListNode(-1)
        node, node1, node2 = new_head, head, head.next
        
        while node1 and node2 and node2.next:
            next_node1 = node2.next
            next_node2 = next_node1.next
            node.next = node2
            node.next.next = node1
            node1.next = None
            node1 = next_node1
            node2 = next_node2
            node = node.next.next

        if node2:
            node.next = node2
            node = node.next
        if node1:
            node.next = node1
            node = node.next
            node1.next = None

        return new_head.next
