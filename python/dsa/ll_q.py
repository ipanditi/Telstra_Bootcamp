class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.front=None
        self.rear=None
        self.size=0
    
    def isEmpty(self):
        return self.front is None
    
    def enqueue(self,data):
        new = Node(data)
        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            new.rear = new
        self.size+=1
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        removed_item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear=None
        self.size-=1
        return removed_item
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("peeking from empty queue")
        return self.front.data
    
    def getSize(self):
        return self.size


q = Queue()
#print(f"IS the queue empty? {q.isEmpty()}")
q.enqueue(5)
q.enqueue(4)
q.enqueue(3)        
print(f"THe front element of the queue is {q.peek()}")
q.dequeue()
print(f"THe front element of the queue is {q.peek()}")
print(f"the size of the queue is {q.getSize()}")
print(f"THe front element of the queue is {q.peek()}")
