class LinkedList:
    def __init__(self):
        self.head=None
    class Node:
        def __init__(self):
            self.value=None
            self.next=None
    def traverse(self):
        h=self.head
        if(h==None):
            return h
        while(h.next!=None):
            h=h.next
        return h
    def add(self,item):
        n=self.Node()
        n.value=item
        if(self.head==None):
            self.head=n
        else:
            h=self.traverse()
            h.next=n
    def print(self):
        h=self.head
        while(h!=None):
            print(h.value)
            h=h.next


