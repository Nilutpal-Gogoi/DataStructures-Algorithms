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

    # This function returns the head of the LinkedList
    def getHead(self):
        return self.head.data

    # PRINT LIST
    def print_lst(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data, end=" ")
            cur_node = cur_node.next

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
    # it as a procedure for printing the linked list in reverse order.

    # ------------------------------------ 2. INSERTION OF LINKED LIST -----------------------------------------
    # 2.1 INSERTING AT HEAD
    def insertAtHead(self, data):
        newNode = Node(data)
        if self.isEmpty():
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
        return

    # 2.2 INSERTING AT TAIL
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
                cursor = None
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






































