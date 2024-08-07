class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.nref = None

class doublyLL:
    def __init__(self):
        self.head = None

    def print_ll(self) :
        if self.head is None:
            print("the linked list is empty!")
        else:
           n=self.head
           while n is not None:
               print(n.data)
               n=n.nref

    def print_ll_reverse(self) :
        if self.head is None:
            print("the linked list is empty!")
        else:
           n=self.head
           while n.nref is not None:
               print(n.data)
               n=n.nref
           while n.pref is not None:
               print(n.data)
               n=n.pref


dl1 = doublyLL()

dl1.print_ll()