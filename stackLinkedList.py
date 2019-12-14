''' Implementing a Stack with LinkedList '''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        self.top = Node(value)
        self.length = 1

    def push(self, value):
        ''' Add a node at the end '''
        newNode = Node(value)
        newNode.next = self.top
        self.top = newNode
        self.length += 1
        return self.printStack()

    def pop(self):
        if (self.top == None):
            return 'Stack Underflow'

        removeTop = self.top
        self.top = removeTop.next
        self.length -= 1
        return removeTop.value

    def peek(self):
        return self.top.value

    def printStack(self):
        presentNode = self.top
        array = []
        while presentNode:
            array.append(presentNode.value)
            presentNode = presentNode.next
        print('Stack:',array)
        return array



myStack = Stack(23)
myStack.push(25)
myStack.push(29)
print('Peek',myStack.peek())
print('Pop',myStack.pop())
myStack.printStack()
print('Peek',myStack.peek())
print('Pop',myStack.pop())

myStack.printStack()
print('Peek',myStack.peek())
#
print('Pop',myStack.pop())
print('Pop',myStack.pop())
myStack.printStack()
