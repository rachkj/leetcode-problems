class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.cache=dict()
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head

    def _remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev

    def _add(self,node):
        node.prev=self.head
        node.next=self.head.next
        node.prev.next=node
        node.next.prev=node

    def get(self,key):
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1
    
    def put(self, key,value):
        if key in self.cache:
            self._remove(self.cache[key])
        node=Node(key,value)
        self._add(node)
        self.cache[key]=node

        if len(self.cache)>self.capacity:
            lru=self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)