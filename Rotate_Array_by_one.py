arr=[1,2,3,4,5]
n=len(arr)-1
list1=[]
for i in range(len(arr)-1,-1,-1):
    list1.append(arr[i])
    break
for j in range(n):
    list1.append(arr[j])
print(list1)

# output is right
# [3, 9, 8, 7, 6, 5, 4, 2, 1]

# janreted by ai
arr = [9, 8, 7, 6, 5, 4, 2, 1, 3]
n = len(arr)

# # Rotate the array in a clockwise direction
# rotated_arr = [arr[-1]] + arr[:-1]

# print(rotated_arr)
i=n-1
j=n-2
while i>0:
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp
    i -=1
    j -=1
print(arr)