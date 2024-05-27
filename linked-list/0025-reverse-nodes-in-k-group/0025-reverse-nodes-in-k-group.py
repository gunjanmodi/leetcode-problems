# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        new_head = ListNode(-1)
        self.helper(new_head, head, k)
        return new_head.next

    def helper(self, new_node, current, k):
        reversed_list, next_node, count = self.reverse_list(current, k)
        if count == 0:
            new_node.next = reversed_list
            self.helper(current, next_node, k)
        else:
            left_out_nodes, _, _ = self.reverse_list(reversed_list, k-count)
            new_node.next = left_out_nodes

    def reverse_list(self, node, count):
        if not node:
            return None, None, count
        prev_node = None
        while node and count > 0:
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
            count -= 1
        return prev_node, node, count
