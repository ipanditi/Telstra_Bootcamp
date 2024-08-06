class Node:
    def __init__(self, seatNo, personName):
        self.seatNo = seatNo
        self.next = None
        self.personName = personName
 
class SeatingTicket:
    def __init__(self):
        self.head  = None
 
    def add_seat(self,seatNo, personName):
        new_node = Node(seatNo, personName)
        if self.head is None  or self.head.seatNo >= seatNo:
            new_node.next = self.head
            self.head = new_node
        else:
            curr_node = self.head
            while(curr_node.next is not None and curr_node.next.seatNo < new_node.seatNo):
                curr_node = curr_node.next
            new_node.next = curr_node.next
            curr_node.next = new_node
 
    def traverse(self):
        curr_node = self.head
        while(curr_node):
            print(curr_node.seatNo, curr_node.personName)
            curr_node = curr_node.next
               
seating = SeatingTicket()
seating.add_seat(10, 'Rishab')
seating.add_seat(20, 'Pandit')
seating.add_seat(15, 'naman')
seating.traverse()