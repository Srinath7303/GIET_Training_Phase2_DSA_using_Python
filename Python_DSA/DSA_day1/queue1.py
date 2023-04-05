class queue:
    def __init__(self,maxsize):
        self.__maxsize=maxsize
        self.__queue=[None]*self.__maxsize
        self.__front=0
        self.__rear=-1
    def isempty(self):
        if(self.__front>self.__rear):
            return True
        return False
    def isfull(self):
        if(self.__rear==self.__maxsize-1):
            return True
        return False
    def enqueue(self,data):
        if(self.isfull()):
            print("queue is full",data,"cannot be added to queue")
        else:
            self.__rear+=1
            self.__queue[self.__rear]=data
            print(data,"is added to queue")
    def dequeue(self):
        if(self.isempty()):
            print("The queue is empty")
        else:
            val = self.__queue[self.__front]
            self.__front+=1
            print(val,"is dequeued")
    def display(self):
        if(self.isempty()):
            print("The queue is empty")
        else:
            for i in range(self.__front,self.__rear+1):
                print(self.__queue[i])
    def maxsize(self):
        return self.__maxsize
q1=queue(4)
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.display()
q1.dequeue()
q1.display()