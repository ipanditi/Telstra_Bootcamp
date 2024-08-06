class Node {
    constructor(seatNo, personName) {
        this.seatNo = seatNo;
        this.personName = personName;
        this.next = null;
    }
}

class SeatingTicket {
    constructor() {
        this.head = null;
    }

    addSeat(seatNo, personName) {
        const newNode = new Node(seatNo, personName);
        
        // If the list is empty or the new node should be the new head
        if (this.head === null || this.head.seatNo >= seatNo) {
            newNode.next = this.head;
            this.head = newNode;
        } else {
            // Traverse the list to find the correct insertion point
            let currNode = this.head;
            while (currNode.next !== null && currNode.next.seatNo < seatNo) {
                currNode = currNode.next;
            }
            newNode.next = currNode.next;
            currNode.next = newNode;
        }
    }

    traverse() {
        let currNode = this.head;
        while (currNode !== null) {
            console.log(currNode.seatNo, currNode.personName);
            currNode = currNode.next;
        }
    }
}

// Example usage
const seating = new SeatingTicket();
seating.addSeat(10, 'Rishab');
seating.addSeat(20, 'Pandit');
seating.addSeat(15, 'naman');
seating.traverse();
