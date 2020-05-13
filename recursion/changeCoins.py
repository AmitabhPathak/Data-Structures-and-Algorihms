def change(target,coins):
    if(target==0):
        return 0
    for coin in coins:
        mx=0
        if(coin<=target):
            mx=max(mx,1+change(target-coin,coins))
            #return mx
    return mx
c=change(10,[1,5,10])
print(c)