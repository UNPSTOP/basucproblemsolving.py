count =0
arr= [1, 17, 10, 13, 10, 5, 16, 8]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]<arr[j]:
            print("1")
        else:
            print("0")