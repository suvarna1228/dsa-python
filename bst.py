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
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ") 
    def delete(self,data,curr):
        if self.key is None:
           print("tree is empty")
           return
        if data<self.key:
            if self.lchild:
                self.lchild=self.lchild.delete(data,curr)
            else:
                print("given node is not present in the tree")
        elif data>self.key:
            if self.rchild:
                self.rchild=self.rchild.delete(data,curr)
            else:
                print("given node is not present in the tree")
        else:
            if self.lchild is None:
                temp=self.rchild
                if curr==data:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            if self.rchild is None:
                temp=self.lchild
                if data==curr:
                    self.key=temp.key
                    self.lchild=temp.lchild
                    self.rchild=temp.rchild
                    temp=None
                    return
                self=None
                return temp
            node=self.rchild
            while node.lchild:
                node=node.lchild
            self.key=node.key
            self.rchild=self.rchild.delete(node.key,curr)
        return self
    def min(self):
        current=self
        while current.lchild:
           current=current.lchild
        print("node with smallest key is:",current.key)
    def max(self):
       current=self
       while current.rchild:
           current=current.rchild
       print("node with largest key is:",current.key) 
def count (node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild) 
root=bst(10)
list1=[20,4,50,45,1,4,6]
for i in list1:
  root.insert(i)
print(count(root))
print("preorder")
root.preorder()
print()
# print("inorder")
# root.inorder()
# print()
# print("postorder")
# root.postorder()
#if count(root)>1:
   #root.delete(20,root.key)
#else:
    #print("can't perform deletion")
#print("after deletion")
root.preorder()
print()
root.max()
root.min()