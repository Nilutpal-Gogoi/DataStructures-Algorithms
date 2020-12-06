class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # This function checks if the LinkedList is empty or not.
    def isEmpty(self):
        while self.head is None:
            return True
        else:
            return False

    # This function returns the data of the head of the LinkedList
    def getHead(self):
        return self.head.data

    # This function returns the starting node of the LinkedList
    def getSelfHead(self):
        return self.head

    # PRINT LIST
    def print_lst(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next
        print("\n")
    # ----------------------------------- 1. TRAVERSAL OF LINKED LIST ---------------------------------------
    # 1.1 Using Iterative Method
    def traverse_iterative(self):
        cursor = self.head
        while cursor is not None:
            print(cursor.data, end=" ")
            cursor = cursor.next

    # 1.2 Using Recursive Method
    def traverse_recursive(self, node):
        if node is None:
            print(" ", end=" ")
        else:
            print(node.data, end=" ")
            self.traverse_recursive(node.next)

    # Here if we interchange the line 40 and line 41 then it will print the reverse of the linked list. So we can
    # use it as a procedure for printing the linked list in reverse order.

    # ------------------------------------ 2. INSERTION OF LINKED LIST -----------------------------------------
    # 2.1 INSERTING AT HEAD (Prepend)
    def insertAtHead(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
        return

    # 2.2 INSERTING AT TAIL  (Append)
    def insertAtTail(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = newNode

    # 2.3 INSERTION AFTER NODE
    def insertAfterNode(self, data, prev_node):  # Here the prev_node is the number of nodes after which we have to
        newNode = Node(data)                     # insert the new node.
        if self.head is None:
            return
        count = 1
        cursor = self.head
        while count < prev_node:
            cursor = cursor.next
            # print(cursor.data)
            cursor += 1
        newNode.next = cursor.next
        cursor.next = newNode

    # ------------------------------------ 3. DELETION OF LINKED LIST -----------------------------------------
    # 3.1 DELETION BY VALUE
    def deletingByValue(self, data):
        # 3.1.1 Node to be deleted is head
        cursor = self.head
        if cursor and cursor.data == data:
            self.head = cursor.next
            cursor.next = None
            return

        # 3.1.2 Node to be deleted is other than the head
        prev = None
        while cursor and cursor.data != data:
            prev = cursor
            cursor = cursor.next
        if cursor is None:
            return
        prev.next = cursor.next
        cursor.next = None
        return

    # 3.2 DELETION WITH POSITION
    def deletingByPosition(self, pos):
        if self.head:
            cursor = self.head
        # 3.2.1 Node to be deleted is at position 0
            if pos == 0:
                self.head = cursor.next
                cursor.next = None
                return
        # 3.2.2 Node to be deleted at some other position
            prev = None
            count = 0
            while cursor and count != pos:
                prev = cursor
                cursor = cursor.next
                count += 1
            if cursor is None:
                return
            prev.next = cursor.next
            cursor = None
            return

    # ------------------------------------ 4. LENGTH OF LINKED LIST -----------------------------------------
    # 4.1 Iterative Method
    def length_iterative(self):
        count = 0
        cursor = self.head
        while cursor:
            cursor = cursor.next
            count += 1
        return count

    # 4.2 Recursive Method
    def length_recursive(self,node):
        if node is None:
            return 0
        return 1 + self.length_recursive(node.next)

    # ------------------------------------ 5. NODE SWAP IN LINKED LIST -----------------------------------------
    def swapTwoNodes(self, key1, key2):
        if key1 == key2:
            return

        # Finding the key1 and storing its position
        prev1 = None
        cursor1 = self.head
        while cursor1 and cursor1.data != key1:
            prev1 = cursor1
            cursor1 = cursor1.next

        # Finding the key2 and storing its position
        prev2 = None
        cursor2 = self.head
        while cursor2 and cursor2.data != key2:
            prev2 = cursor2
            cursor2 = cursor2.next

        if not cursor1 or not cursor2:
            return

        # There are two corner cases that we have to keep in mind:
            # 1. Node 1 and Node 2 are not head nodes.
            # 2. Either Node 1 and Node 2 is a head node.
        if prev1:
            prev1.next = cursor2
        else:
            self.head = cursor2

        if prev2:
            prev2.next = cursor1
        else:
            self.head = cursor1

        cursor1.next, cursor2.next = cursor2.next, cursor1.next


llist = LinkedList()
llist.insertAtTail("A")
llist.insertAtTail("B")
llist.insertAtTail("C")
llist.insertAtTail("D")
llist.insertAtTail("E")
llist.insertAtTail("F")

# llist.traverse_recursive(llist.getSelfHead())  # This is for traversing the linkedlist
llist.print_lst()

llist.swapTwoNodes("B", "E")
llist.print_lst()

llist.swapTwoNodes("A","B")
llist.print_lst()

llist.swapTwoNodes("C","C")
llist.print_lst()



































