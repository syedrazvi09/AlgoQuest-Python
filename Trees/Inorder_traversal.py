class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)


A.left = B
A.right = C
B.left = D
B.right = E
C.left = F


def in_order(node):
    if node is None:
        return

    in_order(node.left)
    print(node)
    in_order(node.right)


in_order(A)
