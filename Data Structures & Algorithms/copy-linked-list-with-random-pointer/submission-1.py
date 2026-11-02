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
        # go through the list normally, populating hashmap with orig:new
        curr = head
        map = {}
        while curr:
            map[curr] = Node(curr.val)
            curr = curr.next
        

        # connect new nodes based on orig connections
        for node in map:
            map[node].next = map[node.next] if node.next else None
            map[node].random = map[node.random] if node.random else None
        
        return map[head] if head else None