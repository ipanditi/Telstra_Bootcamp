class Node:
    def __init__(self, by, date, message):
        self.by = by
        self.date = date
        self.message = message
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, by, date, message):
        # Create a new Node with email details
        new = Node(by, date, message)
        # Insert the new Node at the top of the stack
        new.next = self.head
        self.head = new

    def read_list(self):
        # Print details of each email in the stack
        curr = self.head
        while curr:
            print(f"By: {curr.by}, Date: {curr.date}, Message: {curr.message}")
            curr = curr.next

    def pop(self):
        # Remove and return the top email in the stack
        if self.head is None:
            return None
        if self.head.next is None:
            removed_node = self.head
            self.head = None
            return (removed_node.by, removed_node.date, removed_node.message)
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next
        prev.next = None
        return (curr.by, curr.date, curr.message)

    def is_empty(self):
        # Check if the stack is empty
        return self.head is None

# Example usage
email_stack = Stack()

# Adding emails to the stack
email_stack.push("Alice", "2024-08-06", "Hello, this is Alice.")
email_stack.push("Bob", "2024-08-05", "Hello from Bob.")
email_stack.push("Charlie", "2024-08-04", "Charlie here.")

print("All emails in the stack:")
email_stack.read_list()

# Popping emails from the stack
print("\nPopped email:")
print(email_stack.pop())  # Should print Charlie's email

print("\nAll emails after popping:")
email_stack.read_list()

# Check if the stack is empty
print("\nIs the stack empty?", email_stack.is_empty())
