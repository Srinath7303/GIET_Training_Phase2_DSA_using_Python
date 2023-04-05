list=[int(i) for i in input().split()]
target=int(input("enter the target element"))
res=1
for i in range(len(list)):
    if(list[i]==target):
        # print("Element foundd at index",i)
        res=0
        break
if(res==1):
    print("The element is not found in the list")

else:
    print("Element foundd at index",i)
