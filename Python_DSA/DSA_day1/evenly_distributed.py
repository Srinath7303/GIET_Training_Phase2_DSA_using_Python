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
            print(data)
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

q1=queue(5)
q1.enqueue(13983)
q1.enqueue(10080)
q1.enqueue(7113)
q1.enqueue(2520)
q1.enqueue(2500)

start=q1.front
end=q1.rear

print("The answer is")
for i in range(start,end+1):
    res=1
    for j in range(1,11):
        if(q1.queue[i]%j!=0):
            res=0
            break
    if(res==1):
        print(q1.queue[i])

