######################
# Binary Search Tree #
######################

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if root.val == data:
            return root
        elif root.val < data:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root

def search(root, data):
    if root is None or root.val == data:
        return root
    if root.val < data:
        return search(root.right, data)
    return search(root.left, data)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

# Driver program to test the above functions
# Let us create the following BST
#    50
#  /     \
# 30     70
#  / \ / \
# 20 40 60 80
 
#r = Node(50)
#r = insert(r, 30)
#r = insert(r, 20)
#r = insert(r, 40)
#r = insert(r, 70)
#r = insert(r, 60)
#r = insert(r, 80)
 
# Print inoder traversal of the BST
#inorder(r)

############
# AVL Tree #
############

class AVLNode(Node):
    def __init__(self, data):
        super().__init__(left, right, data)
        self.height = 1
