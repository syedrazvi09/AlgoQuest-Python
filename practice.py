class SinglyNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(5)
C = SinglyNode(7)

head.next = A
A.next = B
B.next = C



cur = head

while cur:
    print(cur)
    cur = cur.next


def display(head):
    cur = head
    elements = []
    while cur:
        elements.append(str(cur.val))
        cur = cur.next
    print(' -> '.join(elements))

display(head)


def search(head, target):
    cur = head
    while cur:
        if cur.val == target:
            return True
        cur = cur.next
    return False

print(search(head, 2))

def removeelement(head, target):
    dummy = SinglyNode(0, head)
    cur = head
    prev = dummy
    while cur:
        if cur.val == target:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next


print(removeelement(head, 3))
display(head)