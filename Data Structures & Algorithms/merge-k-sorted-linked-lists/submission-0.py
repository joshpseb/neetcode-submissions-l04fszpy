# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = [] # store node.val, node

        i = 0
        for l in lists:
            curr = l
            while curr:
                heapq.heappush(heap, (curr.val, i, curr))
                i += 1
                curr = curr.next
        
        head = ListNode()
        curr = head
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
        return head.next