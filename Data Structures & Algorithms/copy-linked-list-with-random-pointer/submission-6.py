"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # time and space O(n)

        # go through the list normally, populating hashmap with orig:new
        curr = head
        oldToNew = { None : None}
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next
        

        # connect new nodes based on orig connections
        node = head
        while node:
            new = oldToNew[node]
            new.next = oldToNew[node.next]
            new.random = oldToNew[node.random]
            node = node.next
        
        return oldToNew[head]