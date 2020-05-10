def large(arr):
    max=cur=arr[0]
    if(len(arr)==0):
        return 0
    for num in arr[1:]:
        cur=max(cur+num,num)
        max=max(cur,max)
    return max
