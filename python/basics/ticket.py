class Ticket:
    def __init__(self,source,destination) -> None:
        self.source=source
        self.destination=destination

class Insurance:
    def __init__(self) -> None:
        self.amount=100

class Waiting(Ticket,Insurance):
    def __init__(self,source,destination) -> None:
        Ticket.__init__(self,source,destination)
        Insurance.__init__(self)
        self.status='Waiting'
    def display(self):
        print(f"The ticket from {self.source} to {self.destination} has the status {self.status}")
    
wt = Waiting("Blore","Chennai")
wt.display()