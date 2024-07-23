arr=[0 ,1 ,4 ,5 ,5, 3 ,0 ,7 ,-3 ,0]
sum1=0
if len(arr)>3:
    while 0 in arr:
        arr.remove(0)
    print(arr)
if len(arr)<=1:
    print(arr)
elif len(arr)==2:
    print(arr[0]*arr[1])
elif len(arr)>=3:
    sum1=arr[0]*arr[1]
    for i in range(2,len(arr)):
        sum1 *=arr[i]
        print(abs(sum1))
