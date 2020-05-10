def check(s):
    un=set()
    for i in s:
        if(i in un):
            return False
        else:
            un.add(i)
    return True
print(check("sbss"))