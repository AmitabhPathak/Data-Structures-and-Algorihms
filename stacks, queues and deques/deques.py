class Deque:
    def __init__(self):
        self.items=[]
    def addFront(self,item):
        self.items.insert(0,item)
    def addRear(self,item):
        self.items.append(item)
    def removeFront(self):
        if(self.isEmpty()):
            return "no items"
        l=self.items[0]
        self.items.remove(l)
        return l
    def removeRear(self):
        if (self.isEmpty()):
            return "no items"
        return self.items.pop()
    def isEmpty(self):
        return self.items==[]