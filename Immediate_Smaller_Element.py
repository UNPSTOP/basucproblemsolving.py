arr1=[]

arr=[4,2,1,5,3]
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>arr[j]:
           arr1.append(arr[j])
           break
        else:
             arr1.append(-1)
print(arr1)
# arr = [5, 6, 2, 3, 1, 7]
# arr1 = []
# for i in range(len(arr)):
#     for j in range(i+1, len(arr)):
#         if arr[i] > arr[j]:
#             arr1.append(arr[j])
#             break
#         else:
#             arr1.append(-1)
#     print(arr1)