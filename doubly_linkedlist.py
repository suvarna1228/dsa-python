class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None

class doublyLL:
    def __init__(self):
        self.head = None

    def print_ll(self) :
        if self.head is None:
            print(" linked list is empty!")
        else:
           n = self.head
           while n is not None:
               print(n.data, "-->",end="")
               n = n.nref

    def print_ll_reverse(self) :
        print()
        if self.head is None:
            print("linked list is empty!")
        else:
           n = self.head
           while n.nref is not None:
               n = n.nref
           while n is not None:
               print(n.data, "-->",end=" ")
               n = n.pref
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linked list is not empty!")

    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
           self.head=new_node
        else:
            new_node.nref= self.head
            self.head.pref = new_node
            self.head = new_node
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
           self.head=new_node
        else:
            n = self.head
            while n.nref is not None:
               n= n.nref
            n.nref = new_node
            new_node.pref = n
dl1 = doublyLL()
dl1.insert_empty(10)
dl1.insert_empty(20)
dl1.print_ll_reverse()
dl1.print_ll()