def pair_sum(l,sum):
    seen=set()
    count=0
    for num in l:
        target=sum-num
        if(target not in seen):
            seen.add(num)
        else:
            count +=1
    return (count)
