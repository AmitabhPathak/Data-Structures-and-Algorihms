def permutation(s):
    out=[]
    if(len(s)==1):
        out=[s]
        return s
    for i,let in enumerate(s):
        for perm in permutation(s[:i]+s[i+1:]):
            out= out +[let+perm]
    return out

s=permutation("ABC")
print(s)
