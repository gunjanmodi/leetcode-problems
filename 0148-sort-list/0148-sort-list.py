# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        return self.divide(head)


    def divide(self, node):
        if not (node and node.next):
            return node
        fast, slow, prev_slow = node, node, None
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        list1, list2 = node, slow
        prev_slow.next = None
        
        return self.do_merge(self.divide(list1), self.divide(list2))

    def do_merge(self, list1, list2):
        dummy = ListNode(-1)
        node = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        while list1:
            node.next = list1
            list1 = list1.next
            node = node.next

        while list2:
            node.next = list2
            list2 = list2.next
            node = node.next
        return dummy.next
        