# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        node, list_len = head, 0
        while node:
            list_len += 1
            node = node.next

        result = []
        for _ in range(k):
            count = list_len // k
            count = count + 1 if list_len % k > 0 else count
            k -= 1
            list_len -= count
            
            current_head, node = head, head
            while node and count > 1:
                head = node
                node = node.next
                count -= 1

            if node:
                head = node.next
                node.next = None
            result.append(current_head)
            
        return result
