def binarySearch(arr, target):
    low = 0
    high = len(arr)-1
    while(low<high):
        mid = (low+high)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]<target):
            high=mid-1
        else:
            low =mid+1
    return -1

r = binarySearch([1,2,3,4],2)
print(r)