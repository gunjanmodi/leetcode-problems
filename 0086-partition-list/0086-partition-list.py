# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        list1_head, list2_head = ListNode(-1), ListNode(-1)
        node1, node2, node = list1_head, list2_head, head

        while node:
            next_node = node.next
            if node.val < x:
                node1.next = node
                node1 = node1.next
            else:
                node2.next = node
                node2 = node2.next

            node = next_node
            
        node1.next = list2_head.next
        node2.next = None
        return list1_head.next
