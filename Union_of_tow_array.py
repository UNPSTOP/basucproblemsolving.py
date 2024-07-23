class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,arr1,arr2):
        #code here
        my_tuple=set(arr1+arr2)
        return len(my_tuple)