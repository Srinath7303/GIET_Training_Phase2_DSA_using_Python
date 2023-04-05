class stack:
    def __init__(self,maxsize):
        self.__maxsize=maxsize
        self.__top=-1
        self.__st=[None]*self.__maxsize
    def isempty(self):
        if(self.__top==-1):
            return True
        return False
    def isfull(self):
        if(self.__top==self.__maxsize-1):
            return True
        return False
    def push(self,data):
        if(self.isfull()):
            print("The stack is full",data,"cant be added")
        else:
            self.__top+=1
            self.__st[self.__top]=data
            print(data,"is pushed")
    def pop(self):
        if(self.isempty()):
            print("The stack is  empty")
        else:
            val= self.__st[self.__top]
            self.__top-=1
            return val
    def top(self):
        return self.__st[self.__top]
    def display(self):
        if(self.isempty()):
            print("The stack is empty")
        else:
            ind=self.__top
            while(ind>=0):
                print(self.__st[ind])
                ind-=1
    def maxsize(self):
        return self.__maxsize
st1=stack(5)
st1.push(1)
st1.push(2)
st1.push(3)
st1.push(4)
st1.push(5)
st1.push(6)
st1.display()
print(st1.pop(),"is popped")
print(st1.top())
