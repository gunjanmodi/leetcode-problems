# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = ListNode(-1)
        new_head.next = head
        prev_node, node = new_head, head
        while node:
            next_node = node.next
            if node.val == val:
                prev_node.next = next_node
                node.next = None
                node = next_node
            else:
                prev_node = node
                node = next_node
        return new_head.next

        