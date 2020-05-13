def change(target,coins,known_results):
    mx=target
    if(target==0):
        return 0
    for coin in coins:
        if(coin<=target):
            if(int(target-coin) in known_results.keys()):
                mx = min(mx, 1 + known_results[target - coin])
            else:

                known_results[target - coin] = change(target - coin, coins,known_results)
                mx = min(mx, 1 + known_results[target - coin])
            #return mx
    return mx
known_results= {}
c=change(10,[1,5],known_results)
print(c)