# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
            
        node, last, list_len = head, None, 0
        while node:
            last = node
            node = node.next
            list_len += 1
        k = k % list_len
        if k == 0:
            return head

        node, prev_node = head, None
        for _ in range(list_len - k):
            prev_node = node
            node = node.next

        new_head = node
        prev_node.next = None
        last.next = head
        return new_head
        