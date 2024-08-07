def partition(arr,low,high):
    pivot = arr[high]
    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return i+1

def quick(arr,low,high):
    if low<high:
        pivot = partition(arr,low,high)
        quick(arr,low,pivot-1)
        quick(arr,pivot+1,high)

arr = [1,5,3,4,8]
quick(arr,0,len(arr)-1)
print(arr)