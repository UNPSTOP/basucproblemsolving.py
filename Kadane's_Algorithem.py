arr=[90 ,64 ,-76, 65, 1, 93 ,-99 ,-76 ,-87 ,88, 63 ,-79 ,85 ,-15 ,4 ,-32 ,69, -22]
sum=0
for i in range(len(arr)):
    sum +=arr[i]
    if sum <0:
        sum=-1
print(sum)