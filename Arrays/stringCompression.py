def compress(s):
    track=s[0]
    new=""
    count=1
    for i in range(len(s)):
        if(i!=len(s)-1):
            if(s[i]==s[i+1]):
                count=count+1
            else:
                new=new +s[i]+str(count)
                count=1
                track=s[i+1]
        else:
            new = new + s[i] + str(count)
            count = 1
            #track = s[i + 1]
    return new
print(compress("AABBBBCCCCC"))