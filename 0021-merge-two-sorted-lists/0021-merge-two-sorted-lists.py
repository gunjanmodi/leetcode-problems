# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        node, node1, node2 = head, list1, list2

        while node1 and node2:
            if node1.val <= node2.val:
                node.next = node1
                node1 = node1.next
            else:
                node.next = node2
                node2 = node2.next
            node = node.next
        
        while node1:
            node.next = node1
            node1 = node1.next
            node = node.next

        while node2:
            node.next = node2
            node2 = node2.next
            node = node.next

        
        return head.next
        