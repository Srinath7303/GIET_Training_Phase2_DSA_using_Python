text = "the sun rises in the east"
vocab = ["sun", "in", "east", "doctor", "day"]
text=text.split()
s=set()
for i in text:
    if i not in vocab:
        s.add(i)
if(len(s)==0):
    print(-1)
else:
    print(s)