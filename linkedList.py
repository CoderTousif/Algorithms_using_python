
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, value):
        """ Add a node at the end """
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self.printList()

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return self.printList()

    def printList(self):
        presentNode = self.head
        array = []
        while presentNode:
            array.append(presentNode.value)
            presentNode = presentNode.next
        print(array)
        print('Length:', self.length)
        return array

    def insertNode(self, index, value):
        if index >= self.length:
            return self.append(value)

        newNode = Node(value)
        previousNode = self.traverse(index)
        presentNode = previousNode.next
        newNode.next = presentNode
        previousNode.next = newNode
        self.length += 1
        return self.printList()

    def traverse(self, index):
        presentNode = self.head
        index -= 1
        for i in range(index):
            presentNode = presentNode.next
        return presentNode

    def removeNode(self,index):
        previousNode = self.traverse(index)
        presentNode = previousNode.next
        previousNode.next = presentNode.next
        self.length -= 1
        self.printList()
        return presentNode

    def reverseList(self):
        first = self.head
        self.tail = first
        second = first.next
        self.tail.next = None
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp

        self.head = first
        return self.printList()


if __name__ == '__main__':
    myLinkedList = LinkedList()

    myLinkedList.append(19)
    myLinkedList.append(27)
    myLinkedList.printList()

    myLinkedList.prepend(35)
    myLinkedList.printList()

    myLinkedList.insertNode(1, 46)
    # print(myLinkedList.length)
    myLinkedList.removeNode(2)

    myLinkedList.reverseList()
