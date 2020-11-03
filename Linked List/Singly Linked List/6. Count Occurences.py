# In this lesson, we investigate how to count the occurrence of nodes with a specified
# data element. We will consider how one may solve this problem in both an iterative
# and recursive manner, and we will code the solution to both of these approached in
# python.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def getSelfHead(self):
        return self.head

    def printlst(self):
        cursor = self.head
        while cursor:
            print(cursor.data, end=" ")
            cursor = cursor.next
        print("\n")

    def insertAtHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
        return

    def countOccurrenceIter(self, data):
        cursor = self.head
        count = 0
        while cursor:
            if cursor.data == data:
                count += 1
            cursor = cursor.next
        return count

    def countOccurrenceRec(self, data ,node):
        if not node:
            return 0
        if node.data == data:
            return 1+ self.countOccurrenceRec(data, node.next)
        else:
            return self.countOccurrenceRec(data, node.next)


lst = LinkedList()
lst.insertAtHead(2)
lst.insertAtHead(4)
lst.insertAtHead(4)
lst.insertAtHead(2)
lst.insertAtHead(1)
lst.insertAtHead(6)
lst.insertAtHead(1)
lst.insertAtHead(1)
# lst.printlst()
print(lst.countOccurrenceIter(2))
# print(lst.countOccurrenceRec(1, lst.getSelfHead()))














