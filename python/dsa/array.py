a = [34,11,19,55,37,48,32]
for i in a[4:]:
    if i%2==0:
        print("Even")
    else:
        print("Odd")
print("Done")

def minimax(arr):
    j = k= arr[0]
    for i in arr:
        if i<j:
            j=i
        elif i>k:
            k=i
    return j,k

print(f"{minimax(a)}")