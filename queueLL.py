class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = self.first
        self.length = 0

    def enqueue(self, value):
        """ Add a node at the end """
        newNode = Node(value)

        if self.first is None:
            self.first = newNode
        else:
            self.last.next = newNode
        self.last = newNode
        self.length += 1

    def dequeue(self):
        """Delete first node at the end"""
        if self.first is None:
            return None

        deleteNode = self.first
        self.first = deleteNode.next
        self.length -= 1
        return deleteNode

    def peek(self):
        return self.first.value

    def printList(self):
        presentNode = self.first
        array = []
        while presentNode:
            array.append(presentNode.value)
            presentNode = presentNode.next
        return array


if __name__ == '__main__':
    myQueue = Queue()
    myQueue.enqueue(69)
    myQueue.enqueue(37)
# print(myQueue.dequeue())
# print(myQueue.dequeue())
# print(myQueue.dequeue())
# print(myQueue.dequeue())
# myQueue.enqueue(45)
# myQueue.enqueue(44)
