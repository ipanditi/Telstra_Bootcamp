class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def addFirst(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        else:
            new.next = self.head
            self.head = new
    
    def addLast(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return 
        curr = self.head
        while(curr.next):
            curr = curr.next
        curr.next = new
     
    def addSpecific(self,data,pos):
        new = Node(data)
        count=0
        if self.head is None:
            self.head = new
            return
        curr = self.head
        while(count!=pos):
            curr = curr.next
            count+=1
        if curr!= None:
            curr_n = curr.next
            curr.next = new
            new.next = curr_n
    
    def readList(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next
    
    def readSpecific(self,pos):
        count=0
        curr = self.head
        while(count!=pos and curr):
            curr = curr.next
            count+=1
        if(curr):
            print(curr.data)
        else:
            print("Index doesnt exist in list")
            
    def updateNode(self,data,pos):
        count=0
        curr = self.head
        while(curr and count!=pos):
            curr = curr.next
            count+=1
        if(curr):
            curr.data=data
        else:
            print("Index not present")
            
    def removeFirst(self):
        if(self.head is None):
            return
        self.head = self.head.next
    
    def removeSpecific(self,pos):
        if(self.head is None):
            return
        curr = self.head
        count=0
        while(curr.next and count+1!=pos):
            curr=curr.next
            count+=1
        if(curr):
            curr.next = curr.next.next
        else:
            print("Index not present")
    
    def removeData(self,data):
        if(self.head is None):
            return
        curr = self.head
        curr_prev = None
        while(curr and self.data!=data):
            curr_prev = curr
            curr = curr.next
        if(curr.next):
            curr_prev.next = curr.next
        else:
            print("Index doesnt exist")
    
node = LinkedList()
node.addFirst(14)
node.readList()
node.addSpecific(23,0)
node.readList()
node.addLast(8)
node.addSpecific(7,2)
node.readList()
node.updateNode(6,1)
node.readList()
node.removeSpecific(2)
node.readList()
        
            
    
    
            
    
    
        