class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Dummy head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from linked list
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # Insert node right after head (front = most recent)
    def _insert_front(self, node):
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._insert_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._insert_front(node)
            return

        if len(self.cache) >= self.capacity:
            # remove LRU node (before tail)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

        new_node = Node(key, value)
        self.cache[key] = new_node
        self._insert_front(new_node)

# Testing LRU Cache
cache = LRUCache(2)

cache.put(1, 10)
cache.put(2, 20)

print(cache.get(1))  # should print 10 (makes 1 most recent)

cache.put(3, 30)     # evicts key 2

print(cache.get(2))  # should print -1
print(cache.get(3))  # should print 30