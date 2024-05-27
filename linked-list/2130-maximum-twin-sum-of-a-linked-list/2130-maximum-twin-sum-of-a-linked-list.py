# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow
        
        node, prev = mid.next, None
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        mid.next = prev

        p1, p2 = head, mid.next
        ans = float('-inf')
        while p1 and p2:
            ans = max(ans, p1.val + p2.val)
            p1 = p1.next
            p2 = p2.next
        return ans
