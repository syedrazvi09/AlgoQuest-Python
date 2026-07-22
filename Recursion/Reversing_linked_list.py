class ListNode:
    def __init__(self, val =0, next = None):
        self.val = val
        self.next = next

    def reverselist(self, head):

        # base case / stopping point
        if head is None or head.next is None:
            return head

        # recursively reverse everything after head
        new_head = self.reverselist(head.next)

        # reverse current connection
        head.next.next = head

        # remove old forward connection
        head.next = None

        return new_head


# create linked list
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)


# object creation
ln = ListNode()
new_head = ln.reverselist(head)

# print reversed list
current = new_head

while current:
    print(current.val, end=" -> ")
    current = current.next

print("None")

