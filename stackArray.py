
class Stack:
    def __init__(self,value):
        self.array = [value]
        self.top = value

    def push(self,value):
        self.array.append(value)
        self.top = value

    def pop(self):
        self.top = self.array[len(self.array)-2]
        return self.array.pop()

    def peek(self):
        return self.top

    def printStack(self):
        print(self.array)


myStack = Stack(5)
myStack.push(45)
myStack.push(35)
myStack.printStack()
# print('Top:', myStack.peek())
print('Popped:', myStack.pop())
print('Top: ', myStack.peek())
# print('Stack')
myStack.printStack()
