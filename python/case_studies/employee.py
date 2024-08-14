class Book:
    def __init__(self,bookName, price):
        self.bookname = bookName
        self.price = price

class Author:
    def __init__(self, authorName, address):
        self.authorName = authorName
        self.address = address
        self.bookList = LinkedList() # LinkedList using Book class 
    
    def add_book(self, book):
        self.bookList.insert_at_end(book)

    def get_books(self):
        return self.bookList.traverse()

class Node:
    def __init__(self, book):
        self.book = book
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, book):
        new_node = Node(book)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def traverse(self):
        current = self.head
        books = []
        while current:
            books.append(current.book)
            current = current.next
        return books

#Pure function
def get_expensive_books(author, threshold=200):
    current = author.bookList.head
    expensive_books = []
    
    while current:
        if current.book.price > threshold:
            expensive_books.append(current.book)
        current = current.next
    
    return expensive_books


if __name__=='__main__':
    # Creating Book objects
    book1 = Book("Harry Potter: Chamber of Secrets", 50)
    book2 = Book("Harry Potter: Goblet of Fire", 30)
    book3 = Book("harry potter: deathly hallows", 34)
    book4 = Book("harry potter: order of phoenix", 870)
    book5 = Book("harry potter: deathly hallows part 2", 760)

    # Creating an Author object
    author = Author("JK Rowling", "London")

    # Adding books to the author's linked list of books
    author.add_book(book1)
    author.add_book(book2)
    author.add_book(book3)
    author.add_book(book4)
    author.add_book(book5)
    
    # Accessing the list of books
    books = author.get_books()

    for book in books:
        print(f"Book Name: {book.bookname}, Price: {book.price}")
    
    expensive_books = get_expensive_books(author)

    for book in expensive_books:
        print(f"Expensive Book Name: {book.bookname}, Price: {book.price}")
