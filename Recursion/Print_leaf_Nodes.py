class TreeNode:
    def __init__(self, val = 0 , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def printleaf(root):
    if root is None:
        return

    if root.left is None and root.right is None:
        print(root.val, end=" ")

    printleaf(root.left)

    printleaf(root.right)


root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(1)
root.right.left = TreeNode(6)

print(printleaf(root))
