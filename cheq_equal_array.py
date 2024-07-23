class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, arr1, arr2) -> bool:
        arr1=sorted(arr1)
        arr2=sorted(arr2)
        if arr1==arr2:
            return True
        return False