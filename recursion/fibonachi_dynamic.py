#cache
n=10
cache=[None]*(n+1)
def fib(n):
    if( n==0  or n==1):
        return n
    if(cache[n]!=None):
        return cache[n]
    cache[n]=fib(n-1)+fib(n-2)

    return cache[n]
f=fib(10)
print(f)