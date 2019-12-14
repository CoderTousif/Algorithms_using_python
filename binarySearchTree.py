from collections import deque


class Node:
    def __init__(self, value: int):
        self.value = value
        self.leftPtr = None
        self.rightPtr = None


class BinarySearchTree:
    def __init__(self, value=None):
        if value is not None:
            self.rootNode = Node(value)
            self.length = 1
        else:
            self.rootNode = None
            self.length = 0

    def insert(self, value: int):
        newNode = Node(value)
        if self.rootNode is None:
            self.rootNode = newNode
            self.length = 1
            return
        presentNode = self.rootNode
        while True:
            if presentNode.value > value:
                if presentNode.leftPtr is None:
                    presentNode.leftPtr = newNode
                    self.length += 1
                    return presentNode.leftPtr.value
                presentNode = presentNode.leftPtr
            else:
                if presentNode.rightPtr is None:
                    presentNode.rightPtr = newNode
                    self.length += 1
                    return presentNode.rightPtr.value
                presentNode = presentNode.rightPtr

    def lookUp(self, value):
        print('Finding', value)
        presentNode = self.rootNode
        while presentNode:
            if presentNode.value == value:
                return True
            elif presentNode.value > value:
                presentNode = presentNode.leftPtr
            else:
                presentNode = presentNode.rightPtr
        return False

    def dfsPreOrder(self, presentNode):
        """pre-order traversal"""
        if presentNode is not None:
            print(presentNode.value, end=' ')
            self.dfsPreOrder(presentNode.leftPtr)
            self.dfsPreOrder(presentNode.rightPtr)

    def dfsInOrder(self, presentNode):
        """in-order traversal"""
        if presentNode is not None:
            self.dfsInOrder(presentNode.leftPtr)
            print(presentNode.value, end=' ')
            self.dfsInOrder(presentNode.rightPtr)

    def dfsPostOrder(self, presentNode):
        """post-order traversal"""
        if presentNode is not None:
            self.dfsPostOrder(presentNode.leftPtr)
            self.dfsPostOrder(presentNode.rightPtr)
            print(presentNode.value, end=' ')

    def bfs(self):
        """Breadth First Search"""
        presentNode = self.rootNode
        array = []     # save result
        queue = deque()
        queue.append(presentNode)

        while len(queue) > 0:   # loop until queue is empty
            presentNode = queue.popleft()
            array.append(presentNode.value)
            if presentNode.leftPtr is not None:
                queue.append(presentNode.leftPtr)
            if presentNode.rightPtr is not None:
                queue.append(presentNode.rightPtr)
        return array

    def bfsRecursive(self, queue, arr):
        if len(queue) == 0:
            return arr
        presentNode = queue.popleft()
        # saving the result
        arr.append(presentNode.value)
        if presentNode.leftPtr is not None:
            queue.append(presentNode.leftPtr)
        if presentNode.rightPtr is not None:
            queue.append(presentNode.rightPtr)

        return self.bfsRecursive(queue, arr)

    def isValidBST(self, aNode):
        # compare if value of left node less than parent node
        if aNode.left.value >= aNode.value:
            return False
        # compare if value of right node greater than parent node
        if aNode.right.value <= aNode.value:
            return False
        return True

    def removeNode(self, value):
        presentNode = self.rootNode
        holdingPtr = None
        while presentNode:
            if presentNode.value > value:
                holdingPtr = presentNode
                presentNode = presentNode.leftPtr
            elif presentNode.value < value:
                holdingPtr = presentNode
                presentNode = presentNode.rightPtr
            elif presentNode.value == value:  # If value is matched
                # Check if it is a leaf node then remove it
                if presentNode.leftPtr is None and presentNode.rightPtr is None:
                    if holdingPtr.rightPtr == presentNode:
                        holdingPtr.rightPtr = None
                    elif holdingPtr.leftPtr == presentNode:
                        holdingPtr.leftPtr = None

                # Check if it only has a left node then bypass pointer
                elif presentNode.leftPtr is not None and presentNode.rightPtr is None:
                    if holdingPtr.leftPtr == presentNode:
                        holdingPtr.leftPtr = presentNode.leftPtr
                    elif holdingPtr.rightPtr == presentNode:
                        holdingPtr.rightPtr = presentNode.leftPtr

                # Check if it has right node then bypass pointer
                elif presentNode.leftPtr is None and presentNode.rightPtr is not None:
                    if holdingPtr.leftPtr == presentNode:
                        holdingPtr.leftPtr = presentNode.rightPtr
                    elif holdingPtr.rightPtr == presentNode:
                        holdingPtr.rightPtr = presentNode.rightPtr

                # Check if it has two node then replace it with successor node
                elif presentNode.leftPtr is not None and presentNode.rightPtr is not None:
                    successor = presentNode.rightPtr

                    while successor:
                        prevNode = successor
                        # Check if successor node is a leaf node then replace it
                        if successor.leftPtr is None:
                            successor.leftPtr = presentNode.leftPtr
                            # successor.rightPtr = presentNode.rightPtr
                            if holdingPtr.rightPtr == presentNode:
                                holdingPtr.rightPtr = successor
                            elif holdingPtr.leftPtr == presentNode:
                                holdingPtr.leftPtr = successor

                        elif successor.leftPtr is not None:

                            successor = successor.leftPtr
                            # if successor.leftPtr == None and successor.rightPtr == None:
                            #     successor.rightPtr = presentNode.rightPtr
                            continue
                        successor = successor.rightPtr
                return presentNode.value
            """
            def remove(self, data):
                if self.root is None:
                    print(f"Given data:{data} is not present in the tree")
                else:
                    root_copy = self.root
                    previous_node = root_copy
                    while root_copy is not None:  # SEARCHING FOR THE GIVEN DATA
                        if root_copy.value == data:
                            break
                        elif root_copy.value > data:
                            previous_node = root_copy
                            root_copy = root_copy.left
                        else:
                            previous_node = root_copy
                            root_copy = root_copy.right
                    if root_copy is None:  # GIVEN DATA NOT PRESENT
                        print(f"Given data:{data} is not present in the tree")
                    else:
                        if root_copy.right is None and root_copy.left is None:  # LEAF NODE
                            if previous_node is root_copy:
                                self.root = None
                            elif previous_node.value > data:
                                previous_node.left = None
                            else:
                                previous_node.right = None
                        elif root_copy.left is None and root_copy.right is not None:  # RIGHT SUB TREE EXIST
                            if previous_node is root_copy:
                                self.root = previous_node.right
                            elif previous_node.value > data:
                                previous_node.left = root_copy.right
                            else:
                                previous_node.right = root_copy.right
                        elif root_copy.left is not None and root_copy.right is None:  # LEFT SUB TREE EXIST
                            if previous_node is root_copy:
                                self.root = previous_node.left
                            elif previous_node.value > data:
                                previous_node.left = root_copy.left
                            else:
                                previous_node.right = root_copy.left
                        else:  # GIVEN DATA HAS BOTH THE CHILDREN
                            successor = root_copy.right
                            prev_node_of_successor = successor
                            while successor.left is not None:  # FINDING SUCCESSOR
                                prev_node_of_successor = successor
                                successor = successor.left
                            prev_node_of_successor.left = successor.right  # AS SUCCESSOR MAY HAVE A RIGHT SUB TREE
                            successor.right = root_copy.right  # ASSIGN THE SUB TREES OF NODE TO BE DELETED TO SUCCESSOR
                            successor.left = root_copy.left  # ASSIGN THE SUB TREES OF NODE TO BE DELETED TO SUCCESSOR
                            if previous_node is not self.root:  # CHECKING IF THE GIVEN NODE IS ROOT 
                                if previous_node.value > data:
                                    previous_node.left = successor
                                else:
                                    previous_node.right = successor
                            else:
                                self.root = successor  # MAKING SUCCESSOR AS NEW ROOT
"""


"""
       9
   4       20
 1   6   15  170
"""
# Driver code
if __name__ == '__main__':
    myBst = BinarySearchTree(9)
    myBst.insert(4)
    myBst.insert(20)
    myBst.insert(1)
    myBst.insert(6)
    myBst.insert(15)
    myBst.insert(170)

    print('Pre Order Traversal')
    myBst.dfsPreOrder(myBst.rootNode)
    print('\nIn Order Traversal')
    myBst.dfsInOrder(myBst.rootNode)
    print('\nPost Order Traversal')
    myBst.dfsPostOrder(myBst.rootNode)
    # print('\n')
    # print('Removed Node:', myBst.removeNode(58))
    # print(myBst.lookUp(55))

    print(myBst.bfs())
    # queue = deque()
    # queue.append(myBst.rootNode)
    # print(myBst.bfsRecursive(queue, []))

