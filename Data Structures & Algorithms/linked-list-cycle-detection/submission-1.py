# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr1 = head
        if not head:
            return False
        curr2 = head.next

        while curr1.next and curr2.next and curr2.next.next:
            curr1 = curr1.next
            curr2 = curr2.next.next
            if curr1 == curr2:
                return True
            if not curr1 or not curr2:
                return False
        return False