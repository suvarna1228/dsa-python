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
    def add_end(self,data,x):
        if self.head is None:
            print("linked list is empty!")
        else:
           n = self.head
           while n is not None: 
               if x==n.data:
                   break
           if n is None:
               print("Given node is not present in dll")
           else:
             new_node=Node(data)
             new_node.nref = n.nref
             new_node.pref = n
             if n.nref is not None:
                 n.nref.pref=new_node
             n.nref=new_node
    def add_before(self,data,x):
        if self.head is None:
            print("linked list is empty!")
        else:
           n = self.head
           while n is not None: 
               if x==n.data:
                   break
           if n is None:
               print("Given node is not present in dll")
           else:
            new_node = Node(data)
            new_node.pref = n
            new_node.nref = n.nref
            if n.pref is not None:
                n.pref.nref = new_node
            else:
                self.head = new_node
                n.pref = new_node
                                              






dl1 = doublyLL()
dl1.add_begin(4)
dl1.add_before(10,4)
dl1.print_ll_reverse()
dl1.print_ll()