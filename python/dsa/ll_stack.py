class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return 
        curr = self.head
        while(curr.next):
            curr = curr.next
        curr.next = new
    
    def readList(self):
        curr = self.head
        while(curr):
            print(curr.data)
            curr = curr.next
            
    def pop(self):
        if(self.head is None):
            return
        if(self.head.next is None):
            return self.head.data
        curr= self.head
        prev=None
        while(curr.next):
            prev=curr
            curr = curr.next
        prev.next=None
        return curr.data

node = Stack()
node.push(2)
node.push(3)
node.readList()
p = node.pop()
node.readList()
p1 = node.pop()
node.readList()
        
            
    
    
            
    
    
        