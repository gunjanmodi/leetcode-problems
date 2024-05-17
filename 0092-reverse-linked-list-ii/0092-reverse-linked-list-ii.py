# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head.next:
            return head

        left_node, right_node = head, head
        prev_left, next_right = None, None

        for _ in range(left - 1):
            prev_left = left_node
            left_node = left_node.next
            right_node = right_node.next
        for _ in range(right - left):
            right_node = right_node.next

        if prev_left:
            prev_left.next = None
        next_right = right_node.next
        right_node.next = None

        updated_list = self.reverse_list(left_node, right - left + 1)
        
        if prev_left:
            prev_left.next = updated_list
        else:
            head = updated_list
        left_node.next = next_right
        return head


    def reverse_list(self, node, count):
        prev_node = None
        for _ in range(count):
            next_node = node.next
            node.next = prev_node
            prev_node = node
            node = next_node
        
        return prev_node
        