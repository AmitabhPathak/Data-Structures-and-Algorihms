class Queue2Stack:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def enque(self,item):
        self.stack1.append(item)
    def deque(self):
        while(len(self.stack1)!=0):
            self.stack2.append(self.stack1.pop())
        r=self.stack2.pop()
        while (len(self.stack2) != 0):
            self.stack1.append(self.stack2.pop())

        return r