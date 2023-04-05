def check_anagram(s,t):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    d2={}
    for i in t:
        if i in d2:
            d2[i]+=1
        else:
            d2[i]=1
    if(d==d2):
        return True
    return False



str1=input()
str2=input()
print(check_anagram(str1,str2))