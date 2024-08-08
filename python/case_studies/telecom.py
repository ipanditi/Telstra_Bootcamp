class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email
 
    def __str__(self):
        return f"Customer(ID: {self.customer_id}, Name: {self.name}, Email: {self.email})"
 
class Employee:
    def __init__(self, employee_id, name, position):
        self.employee_id = employee_id
        self.name = name
        self.position = position
 
    def __str__(self):
        return f"Employee(ID: {self.employee_id}, Name: {self.name}, Position: {self.position})"
 
class Service:
    def __init__(self, service_id, service_name):
        self.service_id = service_id
        self.service_name = service_name
 
    def __str__(self):
        return f"Service(ID: {self.service_id}, Name: {self.service_name})"
 
class Payment:
    def __init__(self, payment_id, amount, date):
        self.payment_id = payment_id
        self.amount = amount
        self.date = date
 
    def __str__(self):
        return f"Payment(ID: {self.payment_id}, Amount: {self.amount}, Date: {self.date})"
 
class Plan:
    def __init__(self, plan_id, plan_name, price):
        self.plan_id = plan_id
        self.plan_name = plan_name
        self.price = price
 
    def __str__(self):
        return f"Plan(ID: {self.plan_id}, Name: {self.plan_name}, Price: {self.price})"
 
class Subscription:
    def __init__(self, subscription_id, customer, plan):
        self.subscription_id = subscription_id
        self.customer = customer
        self.plan = plan
 
    def __str__(self):
        return f"Subscription(ID: {self.subscription_id}, Customer: {self.customer.name}, Plan: {self.plan.plan_name})"
 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        self.head = None
 
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
 
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
 
    def find(self, entity_id, key):
        current = self.head
        while current:
            if getattr(current.data, key) == entity_id:
                return current.data
            current = current.next
        return None
 
    def delete(self, entity_id, key):
        current = self.head
        prev = None
        while current:
            if getattr(current.data, key) == entity_id:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False
 
    def update(self, entity_id, key, new_data):
        entity = self.find(entity_id, key)
        if entity:
            for attr, value in new_data.items():
                setattr(entity, attr, value)
            return True
        return False
 
customer1 = Customer(1, "Alice", "alice@example.com")
employee1 = Employee(1, "Bob", "Technician")
service1 = Service(1, "Internet")
payment1 = Payment(1, 100, "2024-08-07")
plan1 = Plan(1, "Basic Plan", 50)
subscription1 = Subscription(1, customer1, plan1)
 
customer_list = LinkedList()
employee_list = LinkedList()
service_list = LinkedList()
payment_list = LinkedList()
plan_list = LinkedList()
subscription_list = LinkedList()
 
customer_list.append(customer1)
employee_list.append(employee1)
service_list.append(service1)
payment_list.append(payment1)
plan_list.append(plan1)
subscription_list.append(subscription1)
 
print("Customers:")
customer_list.display()
 
found_customer = customer_list.find(1, 'customer_id')
print("\nFound Customer:")
print(found_customer)
 
customer_list.update(1, 'customer_id', {'email': 'alice.new@example.com'})
print("\nUpdated Customer:")
customer_list.display()
 
customer_list.delete(1, 'customer_id')
print("\nCustomers after deletion:")
customer_list.display()