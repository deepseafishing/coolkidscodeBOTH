class Node:

    def __init__(self, key, value):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value


class DoublyLinkedList:

    def __init__(self):
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def delete(self, key):
        pass

    def addToFront(self, key):
        pass

    def deleteFromBack(self, key):
        pass


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = DoublyLinkedList()
        self.cache = {}

    def get(self, key: int) -> int:
        if (key in self.cache):
            val = self.cache[key].val
            self.nodes.delete(key)
            self.nodes.addToFront(key, val)
            return val
        return

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.nodes.delete(key)
            self.nodes.addToFront(key)
        else:
            if (len(self.cache) == self.capacity):
                key_to_remove = self.nodes.tail.prev.key
                self.nodes.delete(key_to_remove)
                del self.cache[key_to_remove]
                self.nodes.addToFront(key)
            self.cache[key] = value
            self.nodes.addToFront(key)

            # Your LRUCache object will be instantiated and called as such:
            # obj = LRUCache(capacity)
            # param_1 = obj.get(key)
            # obj.put(key,value)
