import time
start = time.time()
arr = [1,3,5,2,4,123456,78798,98907986,76287468,886768,65327,65724,76328647,57652765,6983762874687,86976297364876983]
maxi=mini=arr[0]
for i in arr:
    if i>maxi:
        maxi=i
    if i<mini:
        mini=i
end = time.time()
m = max(arr)
endd = time.time()
print(maxi,mini)
#print(m)
print(end-start)
print(endd-end)
