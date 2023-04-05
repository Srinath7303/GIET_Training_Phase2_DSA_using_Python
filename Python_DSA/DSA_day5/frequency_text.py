text=input()
text=text.split()
d={}
for i in text:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

d=dict(sorted(d.items(),key=lambda kv:(kv[1]),reverse=True))
d=dict(sorted(d.items(),key=lambda kv:(kv[0])))
print(d)
for i,j in d.items():
    print(i," ",j)
    break