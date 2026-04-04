class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        cur = self.cache[key]
        self.remove(cur)
        self.insert(cur)
        return self.cache[key].val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
        
                
