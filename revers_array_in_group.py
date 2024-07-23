class Solution:
    # Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, k):
        k=k-1
        list1=[]
        list2=[]
        arr=[]
        if k >= len(arr):
            for i in range(len(arr)-1,-1,-1):
                list1.append(arr[i])
            return[list1]
        else:
            for j in range(k,-1,-1):
                list1.append(arr[j])
            for k in range(len(arr)-1,k,-1):
                list2.append(arr[k])
            arr3=list1+list2
        return arr3
# Create a class object
obj = Solution()

# Define the input array and k
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3

# Run the program
result = obj.reverseInGroups(arr, k)
print(result)