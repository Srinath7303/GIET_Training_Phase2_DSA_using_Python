class node:
    def __init__(self,data=None):
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
   


l1=linkedlist()
l1.atend(10)
l1.atend(20)
l1.atend(30)
l1.atend(40)
l1.atend(50)

dummy=node()
l1.listprint()
print()
while(l1.headval!=None):
    Next=l1.headval.next
    l1.headval.next=dummy
    dummy=l1.headval
    l1.headval=Next

while(dummy.next!=None):
    print(dummy.data,end=" ")
    dummy=dummy.next
    