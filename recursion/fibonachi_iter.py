def fib(n):
    a=0
    b=1
    for i in range(n):
        temp=b
        b=b+a
        a=temp
    return a
f=fib(10)
print(f)