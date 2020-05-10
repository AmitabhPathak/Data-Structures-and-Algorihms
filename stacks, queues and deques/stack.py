class Stack:
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if(len(self.items)!=0):
            return self.items.pop()
        else:
            return "UnderFlow"
    def peek(self):
        if (len(self.items) != 0):
            return self.items[-1]
        else:
            return "UnderFlow"
    def isEmpty(self):
        return self.items==[]
    def size(self):
        return len(self.items)