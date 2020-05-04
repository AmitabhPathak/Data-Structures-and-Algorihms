def pair_sum(l,sum):
    count=0
    for i in range(len(l)-1):
        if(sum-l[i] in l[i+1:]):
            count +=1
    return (count)

