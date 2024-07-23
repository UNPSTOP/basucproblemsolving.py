arr=[5,1,1,2,1,1,1]
n=len(arr)
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if arr[i]<arr[j] and arr[j]>arr[k]:
                print(arr.index(arr[j]))
            break
        else:
            pass
            