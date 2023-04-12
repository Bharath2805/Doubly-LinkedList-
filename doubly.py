# Create a node
class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None # next node reference
        self.pref=None # previous node reference

#create a Doubly LinkedList
 
class DoublyLinkedList :
    def __init__(self):
        self.head = None

# traversing forward

    def traversing_forward(self):
        if self.head == None:
            print("DoublyLinkedList is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"-->",end="")
                n=n.nref
# traversing backward
    
    def traversing_backward(self):
        print
        if self.head == None:
            print("DoublyLinkedList is empty")
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.pref

# insert when DoublyLinkedList is empty
    
    def insert_empty(self,data):
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("DoublyLinkedList is not empty")

# insert at begin

    def add_begin(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

# adding at end

    def add_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node 
        else:
            n = self.head
            while n.nref is not None:
                n=n.nref
            n.nref = new_node
            new_node.pref = n

# add after element

    def add_after(self,data,x):
        if self.head == None:
            print("DoublyLinkedList is empty")
        else:
            n=self.head
            while n is not None:
                if x == n.data :
                    break
                n=n.nref
            if n is None:
                print("given node is not present")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = new_node
                if n.nref is not None:  # checking we are inserting in last or not
                    n.nref.pref = new_node
                n.nref = new_node

# add befor element
   
    def add_before(self,data,x):
        if self.head == None:
            print("DoublyLinkedList is empty")
        else:
            n=self.head
            while n is not None:
                if x == n.data :
                    break
                n=n.nref
            if n is None:
                print("given node is not present")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node


    





                 




        