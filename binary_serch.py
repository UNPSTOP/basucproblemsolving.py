class Solution:
    def binarysearch(self, arr, k):
        # Code Here
        for i in range (len(arr)):
            if arr[i]==k:
                return i
        return -1