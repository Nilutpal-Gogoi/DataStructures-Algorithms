# Remove duplicates from the Linked List
# If the given linked list is: 1-6-1-4-2-2-4, then after solving the linked list will
# look like 1-6-4-2


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
        return

    def print_lst(self):
        cursor = self.head
        while cursor:
            print(cursor.data, end=" ")
            cursor = cursor.next
        print("\n")
        return

    def removeDuplicates(self):
        cursor = self.head
        duplicate = dict()
        prev = None
        while cursor:
            if cursor.data in duplicate:
                prev.next = cursor.next
                cursor = None
            else:
                duplicate[cursor.data] = 1
                prev = cursor
            cursor = prev.next  # Here we don't use cursor.next because there may be a time
# when cursor become None, so that will fetch error.


lst = LinkedList()
lst.insertAtHead(2)
lst.insertAtHead(4)
lst.insertAtHead(4)
lst.insertAtHead(2)
lst.insertAtHead(1)
lst.insertAtHead(6)
lst.insertAtHead(1)
lst.print_lst()
lst.removeDuplicates()
lst.print_lst()












