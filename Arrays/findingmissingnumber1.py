def findmissing(l1,l2):
    dic={}
    for num in l2:
        dic[num]+=1
    for num in l2:
        if(dic[num]==0):
            return num
        else:
            dic[num] -= 1