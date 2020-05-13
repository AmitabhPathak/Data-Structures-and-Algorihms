def change(target,coins):
    mx=target
    if(target==0):
        return 0
    for coin in coins:
        if(coin<=target):
            mx=min(mx,1+change(target-coin,coins))
            #return mx
    return mx
c=change(10,[1,5])
print(c)