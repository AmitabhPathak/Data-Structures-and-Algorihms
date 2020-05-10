class Node:
    def __init__(self):
        self.value=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def add(self,item):
        newNode = Node()
        newNode.value = item
        if(self.head==None):

            self.head=newNode
        else:
            h=self.head
            while(h.next):
                h=h.next
            h.next=newNode
    def print(self):
        h=self.head
        while(h):
            print(h.value)
            h=h.next
    def reverse(self):
        h=self.head
        prev= None
        cur=h
        while(cur):
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        self.head=prev
l=LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.print()
l.reverse()
print("====")
l.print()
