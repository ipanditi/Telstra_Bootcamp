def insertionSort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j=i-1
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
arr=[6,3,2,5,7,9]
insertionSort(arr)
print(arr)
                