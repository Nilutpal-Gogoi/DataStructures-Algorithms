# Find the Nth-to-Last Node from a linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlst(self):
        cursor = self.head
        while cursor:
            print(cursor.data, end=" ")
            cursor = cursor.next
        return

    def insertAtHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head.next
            self.head = newNode
        return

    # ----------- Method 1: Double Iteration -------------------------
    def nthFromLast1(self, n):
        cursor = self.head
        length = 0
        while cursor:
            length += 1
            cursor = cursor.next
        cursor = self.head
        while cursor:
            if length == n:
                return cursor.data
            length -= 1
            cursor = cursor.next
        if cursor is None:
            return

    # ------------ Method 2:  One Pass with Two Pointers ---------------------
    def nthFromLast2(self, n):
        fast = self.head
        slow = self.head
        count = 0
        while fast:
            count += 1
            if count >= n:
                break
            fast = fast.next
        if not fast:
            print(str(n) + " is greater than the number of nodes in list.")
            return
        while fast.next and slow:
            fast = fast.next
            slow = slow.next
        return slow.data


lst = LinkedList()
lst.insertAtHead(2)
lst.insertAtHead(4)
lst.insertAtHead(4)
lst.insertAtHead(2)
lst.insertAtHead(1)
lst.insertAtHead(6)
lst.insertAtHead(1)
print(lst.NthFromLast2(4))



