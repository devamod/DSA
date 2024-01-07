class Node:
    """
    An object for storing a single node of a binary tree
    Models three attributes - Data , link to the right elment and link to the left element
    """
    def __init__(self, data) -> None:
        self.data = data
        self.right = None
        self.left = None

    def __repr__(self) -> str:
        return (f"Node data: {self.data}")    


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print(' ' * 4 * level + '-> ' + str(node.data))
        printTree(node.left, level + 1)    


def inOrder_iterative(root):
    current = root
    # intialize the stack
    stack = []

    while True:
        # reach the left most node of the current node
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print (current.data , end = " ")
            current = current.right
        else:
            break
    
    print()


def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # Then print the data of node
        print(root.data, end=" "),
 
        # Now recur on right child
        printInorder(root.right)


def inorderTraversal(root):
    answer = []

    inorderTraversalUtil(root, answer)
    print(answer)

def inorderTraversalUtil(root, answer):

    if root is None:
        return

    inorderTraversalUtil(root.left, answer)
    answer.append(root.data)
    inorderTraversalUtil(root.right, answer)
    return


def preOrder_iterative(root):
    if root == None:
        return []
    # initialize the stack
    stack = [root]

    while stack:
        current = stack.pop()  
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)  
        print(current.data , end = ' ')  

    print()    


def breadthFirst(root):
    # check if the root is None
    if root is None:
        return 
    # initialize a queue
    queue = [root]

    while queue:
        # pop the first element and analyze it 
        current = queue.pop(0)
        print(current.data, end = ' ')
        
        # enque left node
        if current.left:
            queue.append(current.left)

        # enque right node
        if current.right:
            queue.append(current.right)
    print() 


def search(root, target):
    # check if the root is None
    if root is None:
        return 
    # initialize a queue
    queue = [root]

    while queue:
        # pop the first element and analyze it 
        current = queue.pop(0)
        # check if current node is target
        if current.data == target:
            return True
        
        # enque left node
        if current.left:
            queue.append(current.left)

        # enque right node
        if current.right:
            queue.append(current.right)
    return False   


def searchRecur(root, target):
    # check if the root is None
    # also base case
    if root is None:
        return False
    current = root

    # check if current node's value is the target
    if current.data == target:
        return True
    
    # if not rucursivley check left and right tree
    return searchRecur(current.left, target) or searchRecur(current.right, target)     


def sumRecur(root):
    if root is None:
        return 0
    return root.data + sumRecur(root.left) + sumRecur(root.right)

def sumIter(root):
     # check if the root is None
    if root is None:
        return 0
    # initialize a queue
    queue = [root]
    total = 0

    while queue:
        # pop the first element and analyze it 
        current = queue.pop(0)
        total += current.data
        
        # enque left node
        if current.left:
            queue.append(current.left)

        # enque right node
        if current.right:
            queue.append(current.right)
    
    return total       
   

def minIter(root):
    if root == None:
        return
    # initialize the stack
    stack = [root]
    min = root.data

    while stack:
        current = stack.pop()
        if current.data < min:
            min = current.data  
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)   
    
    return min


def minRecur(root):
    if root is None:
        return float('inf')
    leftMin = minRecur(root.left)
    rightMin = minRecur(root.right)

    return min(root.data, leftMin, rightMin)

def maxValuePath(root):
    if root is None:
        return float('-inf')
    if root.right is None and root.left is None:
        return root.data
    maxChildPathSum = max(maxValuePath(root.left), maxValuePath(root.right))
    return root.data + maxChildPathSum

a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

root = Node(5)
root.left = Node(11)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(15)
root.right.right = Node(12)

printTree(root)
MaxSum = maxValuePath(root)
print(MaxSum)
