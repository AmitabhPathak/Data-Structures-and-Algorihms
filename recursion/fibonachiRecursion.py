def feb(n):
    if(n==0 or n==1):
        return n
    else:
        return feb(n-1)+feb(n-2)

f=feb(10)
print(f)