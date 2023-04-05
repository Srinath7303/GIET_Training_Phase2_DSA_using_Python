def binsearch(list,target,start,end):
    mid=start+(end-start)//2
    while(start<=end):
        if(list[mid]==target):
            return mid
        elif(list[mid]>target):
            end=mid-1
        else:
            start=mid+1
        
        mid=start+(end-start)//2
    
    return -1

list=[int(i) for i in input().split()]
target=int(input("enter the target element"))
list.sort()
val= binsearch(list,target,0,len(list)-1)
if(val==-1):
    print("element is not found")
else:
    print("Element found at index",val)