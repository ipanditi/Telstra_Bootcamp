class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}
class LinkedList {
    constructor() {
        this.head = null;
    }
 
    add(data) {
        const newNode = new Node(data);
        if (this.head === null) {
            this.head = newNode;
        } else {
            let current = this.head;
            while (current.next !== null) {
                current = current.next;
            }
            current.next = newNode;
        }
    }
 
    findById(id, attribute) {
        let current = this.head;
        while (current !== null) {
            if (current.data[attribute] === id) {
                return current.data;
            }
            current = current.next;
        }
        return null;
    }
 
    update(id, newData, attribute) {
        let current = this.head;
        while (current !== null) {
            if (current.data[attribute] === id) {
                Object.assign(current.data, newData);
                return;
            }
            current = current.next;
        }
    }
 
    delete(id, attribute) {
        if (this.head === null) return;
 
        if (this.head.data[attribute] === id) {
            this.head = this.head.next;
            return;
        }
 
        let current = this.head;
        while (current.next !== null && current.next.data[attribute] !== id) {
            current = current.next;
        }
 
        if (current.next !== null) {
            current.next = current.next.next;
        }
    }
 
    display() {
        let current = this.head;
        while (current !== null) {
            console.log(current.data);
            current = current.next;
        }
    }
}
 
class Customer {
    constructor(customerID, name, address, phone) {
        this.customerID = customerID;
        this.name = name;
        this.address = address;
        this.phone = phone;
    }
}
 
class Employee {
    constructor(employeeID, name, department, position) {
        this.employeeID = employeeID;
        this.name = name;
        this.department = department;
        this.position = position;
    }
}
 
class Service {
    constructor(serviceID, name, description, cost, outletID) {
        this.serviceID = serviceID;
        this.name = name;
        this.description = description;
        this.cost = cost;
        this.outletID = outletID;
    }
}
 
class Plan {
    constructor(planID, name, dataLimit, cost) {
        this.planID = planID;
        this.name = name;
        this.dataLimit = dataLimit;
        this.cost = cost;
    }
}
 
class Subscription {
    constructor(subscriptionID, startDate, endDate, customerID, planID, serviceID, outletID) {
        this.subscriptionID = subscriptionID;
        this.startDate = startDate;
        this.endDate = endDate;
        this.customerID = customerID;
        this.planID = planID;
        this.serviceID = serviceID;
        this.outletID = outletID;
    }
}
 
class Payment {
    constructor(paymentID, amount, date, subscriptionID) {
        this.paymentID = paymentID;
        this.amount = amount;
        this.date = date;
        this.subscriptionID = subscriptionID;
    }
}
 
class Outlet {
    constructor(outletID, location, manager, employeeID) {
        this.outletID = outletID;
        this.location = location;
        this.manager = manager;
        this.employeeID = employeeID;
    }
}
 
 
const customerList = new LinkedList();
const employeeList = new LinkedList();
const serviceList = new LinkedList();
const planList = new LinkedList();
const subscriptionList = new LinkedList();
const paymentList = new LinkedList();
const outletList = new LinkedList();
 
 
const newCustomer = new Customer(1, 'Nama', 'hsr layout', '9086052258');
customerList.add(newCustomer);
 
 
const foundCustomer = customerList.findById(1, 'customerID');
console.log('Found Customer:', foundCustomer);
 
 
customerList.update(1, { name: 'Nata' }, 'customerID');
 
 
customerList.delete(1, 'customerID');
 
customerList.display();