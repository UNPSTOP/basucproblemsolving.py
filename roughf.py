# # def reverseInGroups(self, arr, N, K):
# #     for i in range(0, N, K):
# #         if N - i < K:
# #             arr[i:] = arr[i:][::-1]
# #         else:
# #             arr[i:i+K] = arr[i:i+K][::-1]
# #     return arr

# # arr = [1, 2, 3, 4, 5]
# # N = len(arr)
# # K = 3
# # print(reverseInGroups(None, arr, N, K))  # Output: [2, 1, 4, 3, 5]a
# arr=[34,48,23,45,6,87,76,65,56,54,45,34]
# def maxn():
#     i=0
#     arr1=0
#     list1=[]
#     while i<len(arr):
#         if arr[i]>arr1:
#             arr1=arr[i]
#         else:
#             list1.append(arr[i])
#         i+=1
#     return arr1
# res=maxn()
# print(res)
# # def max2():
# #     list1=[1,2,3,4]
# #     maxn()
# #     return maxn(list1)
    
# # result1=max2()
# # print(result1)

arr=[2,4,1,3,5]
frist=0
second=0
third=0
for num in arr:
    if num>frist:
        third=second
        second=frist
        frist=num
        print(third)
    elif num > second and num !=frist:
        third=second
        second=num
    elif num > third and num !=second and num !=frist:
        third=num
if third != float('-inf'):
    print("the third largest elment  is ",third)
else:
    print("not enough uniqe element")

print(frist,second,third)
















