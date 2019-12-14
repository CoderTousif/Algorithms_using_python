class Node:
    def __init__(self, value):
        self.value = value
        self.leftPtr = None
        self.rightPtr = None

class BinaryTree:
    def __init__(self, value):
        self.rootNode = Node(value)
        self.lastNode = self.rootNode
        self.length = 1

    def addNode(self, value):
        newNode = Node(value)
        if self.lastNode.leftPtr == None:
            self.lastNode.leftPtr = newNode
            print('Left:', self.lastNode.leftPtr.value)
        elif self.lastNode.rightPtr == None:
            self.lastNode.rightPtr = newNode
            print('right:', self.lastNode.rightPtr.value)
        # self.lastNode = newNode
        self.length += 1
        #
        # while presentNode != None:
        #     presentNode = presentNode.leftPtr
        # if presentNode.leftPtr == None:
        #     presentNode.leftPtr = newNode
        #     print('Left:', presentNode.leftPtr.value)
        # else:
        #     presentNode.rightPtr = newNode
        #     print('Right:', presentNode.leftPtr.value)
        # self.length += 1



myTree = BinaryTree(50)
myTree.addNode(46)
myTree.addNode(56)
# myTree.addNode(55)
# myTree.addNode(44)
print(myTree.length)
