def findmissing(l1,l2):
    result=0
    for num in l1+l2:
        result ^=num
    return result