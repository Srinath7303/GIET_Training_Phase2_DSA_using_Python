class node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
class slinkedlist:
    def __init__(self):
        self.headval=None
    def listprint(self):
        printval=self.headval  #temp
        while printval is not None:
            print(printval.data)
            printval=printval.next
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
            while(temp.next!=None):
                temp=temp.next
            temp.next=newnode
    def atposition(self,data,pos):
        newnode=node(data)
        cnt=1
        if(pos==1):
            self.athead(data)
        else:
            temp=self.headval
            while(cnt<pos-1):
                temp=temp.next
                cnt+=1
            if(temp.next==None):
                self.atend(data)
            
            newnode.next=temp.next
            temp.next=newnode





          
list=slinkedlist()
e1=node("tue")
e2=node("wed")
list.headval.next=e1
e1.next=e2
list.athead('sun')
list.atend('fri')
list.atposition('thur',5)
list.listprint()
