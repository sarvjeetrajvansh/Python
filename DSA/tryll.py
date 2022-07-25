class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList : 
    def __init__(self):
        self.head = None
        
    def add_at_front(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def add_at_back(self,data):
        new_node = Node(data)
        
        if self.head == None : 
            self.head = new_node
            return
        tail = self.head
        while(tail.next):
            tail = tail.next
        tail.next = new_node
        
    def printll(self):
        temp = self.head
        while(temp):
            print(temp.data , end="->")
            temp=temp.next
    def lengthll(self):
        temp = self.head
        count = 0
        while(temp):
            count+=1
            temp=temp.next
        print(f"Size of List is : {count} ")
        
    def search(self,key):
        temp = self.head
        index = 0 
        while(temp):
            if temp.data == key :
                print(f"Found At Index : {index}")
                return
            temp = temp.next
            index +=1
        print("Not Found !!")
        

if __name__=='__main__':
    
    lla = LinkedList()
    llb = LinkedList()
    
    elements_in_ll = int(input("Enter No. of Elements in list :  "))
    i=0
    while( i < elements_in_ll):
        #data = int(input("Enter ListItems : "))
        lla.add_at_back(data=i+1)
        llb.add_at_front(data=i+i)
        i+=1
    lla.printll()
    llb.printll()  
    llb.lengthll()
    lla.lengthll()
    lla.search(1)
    llb.search(10)
    