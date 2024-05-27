# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappop, heappush


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, list_head in enumerate(lists):
            if list_head: heappush(min_heap, (list_head.val, i))
        
        new_head = ListNode(-1)
        node = new_head
        while min_heap:
            val, list_idx = heappop(min_heap)
            min_val_node = lists[list_idx]
            next_min_val_node = lists[list_idx].next
            min_val_node.next = None
            node.next = min_val_node
            node = node.next
            lists[list_idx] = next_min_val_node
            if lists[list_idx]:
                heappush(min_heap, (lists[list_idx].val, list_idx))
        return new_head.next
        