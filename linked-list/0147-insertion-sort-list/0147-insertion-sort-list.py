# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorted_head = ListNode(float('-inf'))

        def insert_in_sorted_list(current):
            node, prev_node = sorted_head, None
            inserted = False
            while node:
                if node.val < current.val:
                    prev_node = node
                    node = node.next
                else:
                    prev_node.next = current
                    current.next = node
                    inserted = True
                    break
            if not inserted:
                prev_node.next = current
                current.next = None
                
        while head:
            next_node = head.next
            insert_in_sorted_list(head)
            head = next_node
        return sorted_head.next
    