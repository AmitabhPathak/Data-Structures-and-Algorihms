def anagram(s1,s2):
    s1=s1.replace(" ","")
    s2=s2.replace(" ", "")
    if(len(s1)==len(s2)):
        for l in s1:
            if l not in s2:
                return False
        return True
    return False

print(anagram("abc","bca"))
