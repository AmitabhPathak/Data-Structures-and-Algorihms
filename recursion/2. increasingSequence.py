def inc(n):
    if(n==0):
        pass
    else:
        
        inc(n-1)
        print(n)
        
inc(int(input()))
