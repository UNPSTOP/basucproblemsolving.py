arr=[1,2,3]
arr=list(set(arr))
# arr.sort()
# n=len(arr)
# if n>3:
#     print( arr[0],arr[1])
# else:
#     print(-1)

n=len(arr)
i=0
minm=0
mini=0
mis=[]
while i <n:
    if arr[i] <minm:
        minm=arr[i]
    else:
        mis.append(arr[i])
    i+=1
i=0
while i<n:
    if arr[i] <mini:
        mini=arr[i]
    else:
        mis.append(arr[i])
    i+1
print(mini,minm)