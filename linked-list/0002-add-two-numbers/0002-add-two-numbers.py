# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode(-1)
        node1, node2, node, carry = l1, l2, new_head, 0
        
        while node1 and node2:
            val = node1.val + node2.val + carry
            carry = 0
            if val > 9:
                carry = val // 10
                val = val % 10
                
            node.next = ListNode(val)
            node1, node2, node = node1.next, node2.next, node.next

        while node1:
            val = node1.val + carry
            carry = 0
            if val > 9:
                carry = val // 10
                val = val % 10
                
            node.next = ListNode(val)
            node1, node = node1.next, node.next

        while node2:
            val = node2.val + carry
            carry = 0
            if val > 9:
                carry = val // 10
                val = val % 10
            node.next = ListNode(val)
            node2, node = node2.next, node.next

        if carry > 0:
            node.next = ListNode(carry)

        return new_head.next
        