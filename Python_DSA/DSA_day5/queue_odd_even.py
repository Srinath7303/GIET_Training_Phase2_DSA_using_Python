class queue:
    def __init__(self,maxsize):
        self.__maxsize=maxsize
        self.qu=[None]*self.__maxsize
        self.front=0
        self.rear=-1
    def isempty(self):
        if(self.rear<self.front):
            return True
        else:
            return False
    def isfull(self):
        if(self.rear==self.__maxsize-1):
            return True
        else:
            return False
    def enqueue(self,data):
        if(self.isfull()):
            print("queue is full")
        else:
            self.rear+=1
            self.qu[self.rear]=data
            print(data,"is added")
    def dequeue(self):
        if(self.isempty()):
            print("queue is empty")
        else:
            val=self.qu[self.front]
            self.front+=1
            return val
        
    def get_max(self):
        return self.__maxsize
    def display(self):
        for i in range(self.front,self.rear+1):
            print(self.qu[i],end=" ")
    
    
q1=queue(7)
q1.enqueue(2)
q1.enqueue(7)
q1.enqueue(9)
q1.enqueue(4)
q1.enqueue(6)
q1.enqueue(5)
q1.enqueue(10)

oddq=queue(q1.get_max())
evenq=queue(q1.get_max())

for i in range(q1.front,q1.rear+1):
    if(q1.qu[i]%2!=0):
        oddq.enqueue(q1.qu[i])
    else:
        evenq.enqueue(q1.qu[i])

oddq.display()
print()
evenq.display()