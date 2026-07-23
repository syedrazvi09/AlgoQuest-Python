class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
def merge_lists(list1, list2):

        # base case
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.val <= list2.val:
        list1.next = merge_lists(list1.next, list2)
        return list1
    else:
        list2.next = merge_lists(list1, list2.next)
        return list2

list1 = ListNode(2)
list1.next = ListNode(5)
list1.next.next = ListNode(7)

list2 = ListNode(3)
list2.next = ListNode(6)
list2.next.next = ListNode(9)

result = merge_lists(list1, list2)

current = result

while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")