class Node:
    def __init__(self):
        self.value=None
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insertLeft(self,value):
        r=self.root
        n=Node()
        n.value=value
        if(self.root==None):
            self.root=n
        elif(self.root.left==None):
            self.root.left=n
        else:
            temp=self.root.left
            self.root.left=n
            self.root.left.left=temp

    def insertRight(self, value):
        r = self.root
        n = Node()
        n.value = value
        if (self.root == None):
            self.root = n
        elif (self.root.right == None):
            self.root.right = n
        else:
            temp = self.root.right
            self.root.right = n
            self.root.right.right = temp
    def getLeftChild(self,head):
        return head.left.value
    def getRightChild(self,head):
        return head.right.value
    def preordertraverse(self,head):
        h=head
        if(h==None):
            return
        print(h.value)
        self.preordertraverse(h.left)

        self.preordertraverse(h.right)
    def inordertraverse(self,head):
        h=head
        if(h==None):
            return
        self.inordertraverse(h.left)
        print(h.value)
        self.inordertraverse(h.right)
    def postodertraverse(self,head):
        h=head
        if(h==None):
            return
        self.postodertraverse(h.left)

        self.postodertraverse(h.right)
        print(h.value)

b=BinaryTree()
b.insertLeft(1)
b.insertLeft(2)
b.insertRight(3)
b.insertLeft(4)
b.insertRight(5)
b.preordertraverse(b.root)
