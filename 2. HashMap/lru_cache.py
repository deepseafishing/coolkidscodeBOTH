
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

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None

    def addToFront(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head


    def deleteFromBack(self):
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = DoublyLinkedList()
        self.cache = {}

    def get(self, key: int) -> int:
        if (key in self.cache):
            val = self.cache[key].value
            self.nodes.delete(self.cache[key])
            self.nodes.addToFront(self.cache[key])
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.nodes.delete(self.cache[key])
            self.nodes.addToFront(self.cache[key])
        else:
            newNode = Node(key, value)
            if (len(self.cache) == self.capacity):
                del self.cache[self.nodes.tail.prev.key]
                self.nodes.deleteFromBack()
            self.cache[key] = newNode
            self.nodes.addToFront(newNode)

    # def __str__(self):
    #     curr = self.nodes.head.next
    #     out = ""
    #     while(curr):
    #         out += str(curr.value) + " | "
    #         curr = curr.next
    #     return out

            # Your LRUCache object will be instantiated and called as such:
            # obj = LRUCache(capacity)
            # param_1 = obj.get(key)
            # obj.put(key,value)


lru = LRUCache(10)
lru.put(1, 1)
lru.put(2, 2)
lru.put(3, 3) #(1, 1), (2, 2) (3, 3)
print(lru)
lru.get(2)
lru.put(4, 4)
print(lru)
lru.put(5, 5)
print(lru)

