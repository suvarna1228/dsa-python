class bst:
    def __init__(self,key):
        self.key = key
        self.lchild=None
        self.rchild=None
    def insert(self,data):
        if self.key is None:
            self.key=data
            return
        if self.key ==data:
            return
        if self.key>data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild=bst(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild=bst(data)
    def search(self,data):
        if self.key == data:
           print("node is found")
           return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("node is not present")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("node is not present")
    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

root=bst(10)
list1=[20,4,50,45,1,4,6]
for i in list1:
  root.insert(i)
root.preorder()