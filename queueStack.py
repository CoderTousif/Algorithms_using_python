
class CrazyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,value):
        self.stack1.append(value)
        self.stack2.append(self.stack1.pop(value))

    def dequeue(self):
        return self.stack1.pop()

    def peek(self):
        top = len(self.stack1) - 1
        return self.stack1[top]

    def printList(self):
        print(self.stack1)


myQueue = CrazyQueue()
myQueue.enqueue(45)
myQueue.enqueue(35)
myQueue.printList()


print('Top',myQueue.peek())
print(myQueue.dequeue())
print('Top',myQueue.peek())
