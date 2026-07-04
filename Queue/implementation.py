from collections import deque

class Queue:

    def __init__(self):
        self._dq = deque()

    def enqueue(self, val):
        self._dq.append(val)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        self._dq.popleft()

    def peek(self):
        if self.is_empty():
            return None
        return self._dq[0]

    def is_empty(self):
        return len(self._dq) == 0

    def size(self):
        return len(self._dq)

    def print_queue(self):
        print("Front -> ", list(self._dq), " <- Rear")

q = Queue()
q.enqueue(24)
q.enqueue(12)
q.enqueue(47)
q.print_queue()