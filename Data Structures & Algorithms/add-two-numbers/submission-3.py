# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        out = ListNode()
        sumPointer = out
        carry = 0
        while curr1 or curr2:
            if not curr1 and curr2:
                curr1 = ListNode(0)
            if curr1 and not curr2:
                curr2 = ListNode(0)
            digitSum = curr1.val + curr2.val + carry
            if digitSum > 9:
                carry = digitSum // 10 # carry
                digitSum -= carry * 10 # sum
            elif digitSum <= 9:
                carry = 0
            sumPointer.val = digitSum
            
            if curr1.next or curr2.next or carry != 0:
                sumPointer.next = ListNode(carry)
                sumPointer = sumPointer.next
            
            curr1 = curr1.next
            curr2 = curr2.next
        return out