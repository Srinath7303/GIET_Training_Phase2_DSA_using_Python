import sys
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        temp=self.headval
        while temp is not None:
            print(temp.data,end=' ')
            temp=temp.next

    def athead(self,data):
        newnode=node(data)
        if(self.headval==None):
            self.headval=newnode
        else:
            newnode.next=self.headval
            self.headval=newnode
    def atend(self,data):
        newnode=node(data)
        if(self.headval==None):
            self.headval=newnode
        else:
            temp=self.headval
            while(temp.next != None):
                temp=temp.next
            temp.next=newnode

    def len(self):
        cnt=0
        temp=self.headval
        while temp is not None:
            cnt+=1
            temp=temp.next
        print(cnt)
   
n=int(input())
l1=linkedlist()
l1.atend(10)
l1.atend(20)
l1.atend(100)
l1.atend(30)
l1.atend(40)
l1.listprint()
max=-1
temp=l1.headval
while temp!=None:
    if(temp.data>max):
        max=temp.data
    temp=temp.next
temp=l1.headval
while temp!=None:
    if(temp.data==max):
        temp.data=n
        break
    temp=temp.next
print()
l1.listprint()