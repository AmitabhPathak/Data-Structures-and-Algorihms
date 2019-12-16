def fact(n):
    if(n==0):
        return 1
    smallFact=fact(n-1)
    ans=smallFact*n
    return ans
print(fact(int(input())))
