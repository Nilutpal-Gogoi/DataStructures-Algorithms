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
            print(cursor.data)





















