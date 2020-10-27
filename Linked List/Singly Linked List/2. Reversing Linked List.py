class Node:
    def __init__(self,data):
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
        print("\n")
        return

    def insertAtHead(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
        return

    # -------------------- Reversing by elements --------------------------------
    def reverse_ele(self):
        lis = []
        temp = self.head
        while temp:
            lis.append(temp.data)
            temp = temp.next
        temp = self.head
        for i in range(len(lis)-1, -1, -1):
            temp.data = lis[i]
            temp = temp.next
        return

# Time Complexity = O(n) ; Space Complexity = O(n) for creating an array.

    # ----------------------- Reversing The Links --------------------------------
    # --------------------- A) Sliding the pointers -------------------------
    # Here we will use three pointers.
    def reverse_links1(self):
        p = self.head
        q = None
        r = None
        while p:
            r = q
            q = p
            p = p.next
            q.next = r
        self.head = q
        return
# Time Complexity = O(n) ; Space Complexity = O(1) for creating an array.

    # ---------------------- B) Using Recursion --------------------------------
    def reverse_rec(self):
        def _recursive(p, q, r):
            if not p:
                return q
            r = q
            q = p
            p = p.next
            q.next = r
            return _recursive(p, q, r)
        self.head = _recursive(self.head, None, None)





lst = LinkedList()
lst.insertAtHead(6)
lst.insertAtHead(5)
lst.insertAtHead(4)
lst.insertAtHead(3)
lst.printlst()
lst.reverse_ele()
lst.printlst()
lst.insertAtHead(2)
lst.printlst()
lst.reverse_links1()
lst.printlst()
lst.insertAtHead(1)
lst.printlst()
lst.reverse_rec()
lst.printlst()























