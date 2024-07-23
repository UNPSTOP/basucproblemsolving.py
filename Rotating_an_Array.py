# arr1= [-1, -2, -3, 4, 5, 6, 7]
# # Inpu
# # t: arr[] = [-1, -2, -3, 4, 5, 6, 7], d = 2
# # Output: [-3, 4, 5, 6, 7, -1, -2]
# # arr = [1,2,3,4,5]
# # d=2
# # list1=[]
# # for i in range(d,len(arr)):
# #     list1.append(arr[i])
# # for j in range(0,d):
# #     list1.append(arr[j])
# # print(list1)
# # end=0
# # n=len(arr)
# # start=0
# def revers(arr,start=0,end=0):
#     while start< end:
#         temp =arr[start]
#         arr[start]=arr[end]
#         arr[end]=temp
#         start +=1
#         end -=1
#     return arr
# def revers2(arr,d,n):
#     revers(arr,0,d-1)
#     revers(arr,d,n-1)
#     revers(arr,0,n-1)
#     return (arr)
# print(revers2(arr=[-1,-2,-3,4,5,6,7],d=3,n=7))
arr=[1,2,3,4,5]
d=2
arr.reverse()

print(arr)
