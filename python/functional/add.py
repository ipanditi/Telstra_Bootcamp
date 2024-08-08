x,y = 23,4
#Pure function
def add(a,b):
    return a+b
#Impure functions
def sum_xy():
    return x+y
print(add(23,4))
print(sum_xy())
#Lambda function
result = lambda x,y: x+y
print(result(12,4))

#Higher order funcs
def callme(f,a,b):
    f(a,b)