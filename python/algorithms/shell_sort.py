def shellSort(arr, n):
    gap=n//2
    while gap>0:
        j=gap
        while j<n:
            i=j-gap 
            while i>=0:
                if arr[i+gap]>arr[i]:

                    break
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
                i=i-gap 
            j+=1
        gap=gap//2

arr = [1,7,6,3,5,4]
shellSort(arr,6)
print(arr)