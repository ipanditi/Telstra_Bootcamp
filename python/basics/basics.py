def marks():    
    marks = int(input("Enter marks: "))
    if marks>=90:
        grade='A'
    elif marks>=75:
        grade='B'
    elif marks>=50:
        grade='C'
    else:
        grade='F'
    print(grade)

def cards():
    card = input('Pick any card Club, Spade, Diamond, Heart,Joker: ')
    map = {'Club':2,'Spade':3,'Diamond':4,'Heart':6,'Joker':10}
    num = map[card]
    print(num)


def odd_even():
    num = int(input('Enter number: '))
    if num%2==0:
        print("Even")
    else:
        print("Odd")
        
def reverse_num(num):
    reverse_num=0
    while num!=0:
        d = num%10
        reverse_num = reverse_num*10 + d
        num //=10
    print(reverse_num)

def pal(s):
    return s == s[::-1]
#print(pal('naman'))

def pali(s):
    stack = []
    n = len(s)
    for e in s:
        stack.append(e)
    for i in range(len(stack)):
        if s[i]!=stack[i]:
            break
    return True
#print(pali('naman'))

def three_digits(arr):
    for i in arr:
        if i<1000 and i>99:
            print(f"{i} has Three digits")
        
def has_three_digits(num):
    num = abs(num)  # Consider the absolute value to handle negative numbers
    # Divide the number until it is less than 1000 and check the count of divisions
    count = 0
    while num >= 100:
        num //= 10
        count += 1
    return count == 2  # Exactly three digits if two divisions are done
array = [123,768,78,90]
# Find numbers with exactly 3 digits
three_digit_numbers = [num for num in array if has_three_digits(num)]
print(three_digit_numbers)