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
    def atval(self,data):
        newnode=node(data)
        if(self.headval==None):
            self.headval=newnode
        else:
            temp=self.headval
            while temp!=None:
                if(temp.data<data and temp.next!=None  and data<temp.next.data):
                    newnode.next=temp.next
                    temp.next=newnode
                    break
                elif(temp.data<data and temp.next==None):
                    self.atend(data)
                    break
                temp=temp.next

    def delete(self,data):
        if(self.headval==data):
            self.headval=self.headval.next
        else:
            temp=self.headval
            while temp.next != None:
                if(temp.next.data==data):
                    temp.next=temp.next.next
                temp=temp.next


    def find(self,data):
        temp=self.headval
        while temp != None:
            if(temp.data==data):
                return True
            temp=temp.next
        return False
    def len(self):
        cnt=0
        temp=self.headval
        while temp is not None:
            cnt+=1
            temp=temp.next
        print(cnt)
   

class bakehouse:
    def __init__(self):
        self.clinked=linkedlist()
    def get_occupied(self):
        self.clinked.listprint()
    def allocate(self):
        for i in range(1,11):
            if(not self.clinked.find(i)):
                val=i
                break
        self.clinked.atval(i)
    def deallocate(self,tablenumber):
        self.clinked.delete(tablenumber)


b1=bakehouse()
b1.allocate()
b1.allocate()
b1.allocate()
b1.allocate()
b1.allocate()
b1.allocate()
b1.get_occupied()
b1.deallocate(2)
print()
b1.get_occupied()
b1.allocate()
print()
b1.get_occupied()