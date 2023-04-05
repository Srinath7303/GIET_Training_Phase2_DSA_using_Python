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
list1=linkedlist()
list2=linkedlist()
list3=linkedlist()
list1.atend(1)
list1.atend(2)
list1.atend(4)
list1.atend(3)
list1.atend(5)
list2.atend(9)
list2.atend(8)
list2.atend(11)

cnt=1
temp=list1.headval
while(cnt<n):
    cnt+=1
    temp=temp.next
newtemp=temp.next
temp.next=list2.headval
temp=list1.headval
while(temp.next !=None):
    temp=temp.next
temp.next=newtemp
list1.listprint()


