class LRUCache:
    # use a linked list
    # if 
    def __init__(self, capacity: int):
        self.cache = {} #key, node

        self.capacity = capacity
        self.currSize = 0

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache: # remove node and add it to last (most recent)
            node = self.cache[key]
            self.remove(node)
            self.addLast(node)
            return node.val
        else: # key not in cache, return -1
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: # remove node, add updated node to last and update cache
            node = self.cache[key]
            self.remove(node)

            newNode = Node(key, value)
            self.addLast(newNode)
            self.cache[key] = newNode
        else: # add new node to last, update cache, remove LRU if capacity over
            newNode = Node(key, value)
            self.addLast(newNode)
            self.cache[key] = newNode
            
            self.currSize += 1
            if self.currSize > self.capacity:
                del self.cache[self.head.next.key]
                self.remove(self.head.next)
                
            


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addLast(self, node):
        last = self.tail.prev

        last.next = node
        node.prev = last
        self.tail.prev = node
        node.next = self.tail

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    
