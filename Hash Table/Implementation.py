class Node:
    def __init__(self, key, val):
        self. key = key
        self.val = val
        self.next = None

class HashTable:
    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    # Insert
    def insert(self, key, val):
        idx = self._hash(key)
        node = self.buckets[idx]

        # walk chain, update if key exists
        while node:
            if node.key == key:
                node.val = val
                return
            node = node.next

        new_node = Node(key, val)
        new_node.next = self.buckets[idx]   # link to old head
        self.buckets[idx] = new_node
        self.size += 1

        if self.size / self.capacity > 0.7:
            self._rehash()

    # Search
    def search(self, key):
        idx = self._hash(key)
        node = self.buckets[idx]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return None

    # Delete
    def delete(self, key):
        idx = self._hash(key)
        prev = None
        node = self.buckets[idx]

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.buckets[idx] = node.next
                self.size -= 1
                return True
            prev = node
            node = node.next
        return False


    # Rehash
    def _rehash(self):
        old = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self.size = 0

        for node in old:
            while node:
                self.insert(node.key, node.val)
                node = node.next

    # Print
    def print_table(self):
        for i, node in enumerate(self.buckets):
            chain = []
            while node:
                chain.append(f"({node.key} : {node.val})")
                node = node.next
            print(f" [{i : 2d}] {' -> '.join(chain) or 'empty'}")

ht = HashTable()

ht.insert("name", "Bruce")
ht.insert("age", 25)
ht.insert("city", "Gotham")

ht.print_table()
