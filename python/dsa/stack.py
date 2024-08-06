class Stack:
    def __init__(self,stack):
        self.stack=stack
        self.top=-1
        
    def push_data(self,data): 
        self.stack.append(data)
        self.top =self.top+ 1

    def pop_data(self):
        p = self.stack.pop()
        return p
    
    def display(self):
        print(self.stack)

s = Stack([1,2,3,4])
s.push_data(2)
rem = s.pop_data()
s.push_data(4)
print(rem)
s.display()