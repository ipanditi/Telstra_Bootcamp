class Message:
    def __init__(self,msg,to) -> None:
        self.msg = msg
        self.to = to
        self.next = None
    
class Queue:
    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.size = 0
    
    def isEmpty(self):
        return self.front is None
    
    def enqueue(self, msg:str, to:str):
        new = Message(msg,to)
        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new
        self.size+=1
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        removed_item = self.front.msg
        self.front = self.front.next
        if self.front is None:
            self.rear=None
        self.size-=1
        return removed_item

    def getSize(self):
        return self.size
    
    def peek(self):
        if self.isEmpty():
            raise IndexError("peeking from empty queue")
        return self.front.msg
    
q = Queue()

q.enqueue("hey","vivek")
print(q.peek())
q.enqueue("hi","ays")
print(q.getSize())
q.enqueue("hey","jain")
print(q.peek())
print(q.dequeue())
print(q.peek())
print(q.getSize())