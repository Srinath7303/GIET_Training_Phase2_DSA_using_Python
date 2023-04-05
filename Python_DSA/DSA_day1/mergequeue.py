class queue:
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.queue=[None]*self.maxsize
        self.front=0
        self.rear=-1
    def isempty(self):
        if(self.front>self.rear):
            return True
        return False
    def isfull(self):
        if(self.rear==self.maxsize-1):
            return True
        return False
    def enqueue(self,data):
        if(self.isfull()):
            print("queue is full",data,"cannot be added to queue")
        else:
            self.rear+=1
            self.queue[self.rear]=data
            
    def dequeue(self):
        if(self.isempty()):
            print("The queue is empty")
        else:
            val = self.queue[self.front]
            self.front+=1
            print(val,"is dequeued")
    def display(self):
        if(self.isempty()):
            print("The queue is empty")
        else:
            for i in range(self.front,self.rear+1):
                print(self.queue[i])
    def max_size(self):
        return self.maxsize

q1=queue(2)
q2=queue(3)
q3=queue(q1.max_size()+q2.max_size())
q1.enqueue(1)
q1.enqueue(2)
q2.enqueue(10)
q2.enqueue(20)
q2.enqueue(30)

while(q1.front<=q1.rear and q2.front<=q2.rear):
     q3.enqueue(q1.queue[q1.front])
     q3.enqueue(q2.queue[q2.front])
     q1.front+=1
     q2.front+=1
while(q1.front<=q1.rear):
    q3.enqueue(q1.queue[q1.front])
    q1.front+=1
while(q2.front<=q2.rear):
    q3.enqueue(q2.queue[q2.front])
    q2.front+=1
q3.display()
