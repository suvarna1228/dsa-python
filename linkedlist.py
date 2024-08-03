class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class linkedlist:
    def __init__(self):
        self.head=None

    def print_ll(self) :
        if self.head is None:
            print("the linked list is empty!")
        else:
           n=self.head
           while n is not None:
               print(n.data)
               n=n.ref
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x== n.data:
              break
            n = n.ref
        if n is None:
            print("node is not present in ll")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("ll is empty")

        if self.head.data==x:
           new_node=Node(data)
           new_node.ref=self.head
           self.head=new_node
           return
        n=self.head
        while n.ref is not None:
            if n.ref.data==x:
                break
            else:
                new_node=Node(data)
                new_node.ref=n.ref
                n.ref=new_node
    
    def insert_empty(self,data):
        if self.head is None:
            new_node=Node(data)
            self.head=new_node
        else:
            print("ll is not empty!")


ll1=linkedlist()
ll1.add_begin(10)
ll1.add_begin(20)
ll1.add_end(100)
ll1.add_end(500)
ll1.insert_empty(10)
ll1.add_begin(30)
ll1.add_after(200,100)
ll1.add_before(20,10)
ll1.print_ll()
