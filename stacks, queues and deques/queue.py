class Queue:
    def __init__(self):
        self.items=[]
    def enque(self,item):
        self.items.append(item)
    def deque(self):
        if(len(self.items)!=0):
           l=self.items[0]
           self.items.remove(l)
           return l
        else:
            return "no items"
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)

