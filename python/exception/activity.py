class Details:
    def __init__(self,name,age,address,email):
        self.name=name
        self.age=age
        self.address=address
        self.email = email
    
    def display(self):
        print(f"The details are: {self.name}, {self.age}")
    
    def checkAge(self):
        if self.age<18:
            raise BaseException("Age cannot be less than 18")
        else:
            print("Age is fine")
    
try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address")
    email = input("Enter your email")
    customer = Details(name,age,address,email)
    customer.checkAge()
    customer.display()

except ValueError:
    print("Invalid datatypes entered.")

except BaseException:
    print("Age is less than 18!")

else:
    print("Try succeeded")

finally:
    print("Yay done!")