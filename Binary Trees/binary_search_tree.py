class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    # Insert a value in binary search tree
    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def preOrderTraversal(root):
    if root is None:
        return
    print(root.info, end=" ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def inOrderTraversal(root): # Ascending order for a BST
    if root is None:
        return
    inOrderTraversal(root.left)
    print(root.info, end=" ")
    inOrderTraversal(root.right)

def postOrderTraversal(root):
    if root is None:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.info, end=" ")

def levelOrderTraversal(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue) > 0:
        print(queue[0].info, end=" ")
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def height(root):
    # Base case:
    # If height = number of vertices then return 0
    # If height = number of edges then return -1
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1

# Validate binary search tree
def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def valid(node, left, right):
        if node is None:
            return True
        if node.val > left and node.val < right:
            return (valid(node.left, left, node.val) and 
                    valid(node.right, node.val, right))
    
    return valid(root, float('-inf'), float('inf'))
