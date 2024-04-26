# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(-101)
        new_head.next = head
        node, prev_node = head, new_head
        
        while node:
            next_node = node.next
            if prev_node.val == node.val:
                prev_node.next = next_node
                node.next = None
            else:
                prev_node = node
            node = next_node
        return new_head.next
        