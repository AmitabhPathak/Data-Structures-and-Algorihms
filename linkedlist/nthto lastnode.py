class Node:
    def __init__(self):
        self.value=None
        self.next=None
class LinkList:
    def __init__(self):
        self.head=None
    def add(self,item):
        h=self.head
        new=Node()
        new.value=item
        if(self.head==None):
            self.head=new
        else:
            while(h.next):
                h=h.next
            h.next=new
    def print(self):
        h=self.head
        while(h):
            print(h.value)
            h=h.next
    def reverse(self):
        h=self.head
        prev=None
        cur=h
        while(cur):
            nxt=cur.nxt
            cur.next=prev
            prev=cur
            cur=nxt
        self.head=prev
    def getNfromLast(self,n):
        cur=self.head
        prev=self.head
        i=1
        while(i<n and cur!=None):
            cur=cur.next
            i +=1
        while(cur.next):
            cur=cur.next
            prev=prev.next
        return prev.value
l=LinkList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.print()
print(l.getNfromLast(3))



