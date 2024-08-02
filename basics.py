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
print(pali('naman'))
