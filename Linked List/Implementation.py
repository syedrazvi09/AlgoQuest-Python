class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Inserting at Head
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Inserting at Tail
    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    # Inserting at the middle
    def insert_after(self, target, data):
        cur = self.head
        while cur:
            if cur.data == target:
                new_node = Node(data)
                new_node.next = cur.next
                cur.next = new_node
                return
            cur = cur.next
        print('Target not found')

    # Traversing the list
    def traverse(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    # Printing the list
    def print_list(self):
        cur = self.head
        parts = []
        while cur:
            parts.append(str(cur.data))
            cur = cur.next
        print('->'.join(parts))

    # Searching a Node
    def search(self, target):
        cur = self.head
        pos = 0
        while cur:
            if cur.data == target:
                return pos
            cur = cur.next
            pos += 1
        return -1   # if node not found

    # Deleting the Head
    def delete_head(self):
        if not self.head:   # if list is empty
            return
        self.head = self.head.next

    # Deleting the Tail
    def delete_tail(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        cur = self.head
        while cur.next.next:
            cur = cur.next
        cur.next = None

    # Delete by Value
    def delete_by_value(self, target):
        if not self.head:
            return
        if self.head.data == target:
            self.head = self.head.next
            return
        prev = None
        cur = self.head
        while cur:
            if cur.data == target:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
        print('Target not found for deleting')

    # Reversing a Linked List
    def reverse(self):
        prev = None
        cur = self.head

        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev





ll = LinkedList()
ll.insert_at_tail(10)
ll.insert_at_tail(20)
ll.insert_at_tail(30)
ll.insert_at_tail(40)
ll.reverse()
ll.print_list()