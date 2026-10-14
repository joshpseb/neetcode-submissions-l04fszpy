# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        node = head
        length = 1
        while node.next:
            node = node.next
            length += 1
        if n == length:
            return head.next

        node = head
        for _ in range(length - n - 1):
            node = node.next
        node.next = node.next.next
      

        return head