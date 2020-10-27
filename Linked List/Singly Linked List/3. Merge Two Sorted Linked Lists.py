# If we are given with two already sorted linked lists, create a third linked list which
# is also sorted.
# Here the two linked lists given will no longer be available in their original form.

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

    def mergeTwoSortedLinkedLists(self, lst2):
        first = self.head    # "first" is a pointer that will move in the first Linked List
        second = lst2.head   # "second" is a pointer that will move in second Linked List
        if not first:
            return second
        if not second:
            return first
        if first.data < second.data:
            third = last = first
            # "third" is a pointer that will act as self.head in the new Linked List
            # "last" is a pointer that will move to form the merged linked list by
            # comparing the data of both linked list
            first = first.next
        else:
            third = last = second
            second = second.next
        while first and second:
            if first.data < second.data:
                last.next = first
                last = first
                first = first.next
            else:
                last.next = second
                last = second
                second = second.next
        if first:
            last.next = first
        else:
            last.next = second
        return third


lst1 = LinkedList()
lst2 = LinkedList()
lst1.insertAtHead(8)
lst1.insertAtHead(6)
lst1.insertAtHead(5)
lst1.insertAtHead(1)
lst2.insertAtHead(7)
lst2.insertAtHead(4)
lst2.insertAtHead(3)
lst2.insertAtHead(2)
lst1.print_lst()
lst2.print_lst()
lst1.mergeTwoSortedLinkedLists(lst2)
lst1.print_lst()