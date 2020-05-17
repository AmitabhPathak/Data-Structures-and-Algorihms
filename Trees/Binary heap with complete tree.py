class BinHeap:
    def __init__(self):
        self.heapList=[0]
        self.size=0
    def balanceup(self,ind):
        while ind//2>0:
            if self.heapList[ind]<self.heapList[ind//2]:
                temp=self.heapList[ind//2]
                self.heapList[ind//2]=self.heapList[ind]
                self.heapList[ind]=temp
            ind=ind//2
    def insert(self,item):
        self.heapList.append(item)
        self.size=self.size+1
        self.balanceup(self.size)
    def min(self,ind):
        if(ind*2+1>self.size):
            return ind*2
        else:
            if self.heapList[ind*2]<self.heapList[(ind*2)+1]:
                return ind*2
            else:
                return ind*2+1

    def balancedown(self,ind):
        while(ind*2<self.size):
            mc=self.min(ind)
            if(self.heapList[ind]>self.heapList[mc]):
                temp=self.heapList[ind]
                self.heapList[ind]=self.heapList[mc]
                self.heapList[mc]=temp
            ind=mc
    def delete(self):
        retvalue=self.heapList[1]
        self.heapList[1]=self.heapList[self.size]
        self.size=self.size-1
        self.heapList.pop()
        self.balancedown(1)
        return retvalue
    def build_heap_from_list(self,li):
        i=len(li)//2
        self.size=len(li)
        self.heapList=[0]+li
        while(i>0):
            self.balancedown(i)
            i=i-1


h=BinHeap()
h.build_heap_from_list([9,6,5,2,3])
print(h.delete())
print(h.delete())
print(h.delete())

