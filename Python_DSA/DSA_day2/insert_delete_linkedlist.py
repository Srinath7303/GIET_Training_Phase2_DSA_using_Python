
class Node:
    def __init__(self, data = None):
        self.dataval = data
        self.nextval = None

class SlinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval,end=' ')
            printval = printval.nextval
        print()


    def Insert_beginning(self, data):
        node = Node(data)
        node.nextval = self.headval
        self.headval = node

    def Insert_end(self,data):
        node = Node(data)
        if(self.headval == None):
            self.headval = Node
        else:
            copy = self.headval
            while copy.nextval is not None:
                copy = copy.nextval
            copy.nextval = node

    def insert_Middle(self,middle,data):
        if(middle is None):
            print("Node is absent")
        else:
            node = Node(data)
            node.nextval = middle.nextval
            middle.nextval = node

    def delete_beginning(self):
        if(self.headval is None):
            print("Linked list empty!")
        else:
            self.headval = self.headval.nextval
    
    def delete_end(self):
        if(self.headval is None):
            print("Linked list is empty!")
        else:
            copy = self.headval
            while copy.nextval.nextval is not None:
                copy = copy.nextval
            copy.nextval = None

   

    def get_count(self,data):
        if(self.headval is None):
            print("Linked list is empty")
        else:
            c = 0
            copy = self.headval
            while copy is not None:
                if(copy.dataval == data):
                    c+=1
                copy = copy.nextval
            return c
lst = SlinkedList()

lst.headval = Node(2)
e2 = Node(3)
e3 = Node(4)

#link part
lst.headval.nextval = e2
lst.headval.nextval.nextval = e3 

print("Before Insertion at beginning")
lst.listprint()
lst.Insert_beginning(1)
print("After Insertion at beginning")
lst.listprint()

print("Before Insertion at end")
lst.listprint()
lst.Insert_end(299)
print("After Insertion at end")
lst.listprint()

print("Before Insertion at middle")
lst.listprint()
lst.insert_Middle(lst.headval.nextval.nextval,300)
print("After Insertion at middle")
lst.listprint()


print("Before delection at starting")
lst.listprint()
lst.delete_beginning()
print("After delection at starting")
lst.listprint()

print("Before delection at end")
lst.listprint()
lst.delete_end()
print("After delection at end")
lst.listprint()





print("Original list")
lst.listprint()
print("The value appears", lst.get_count(300))

