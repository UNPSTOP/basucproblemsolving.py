// User function template for C++

class Solution {
  public:
    int binarysearch(vector<int> &arr, int k) {
        int low=0;
        int high=sizeof(arr)/sizeof(arr[0])-1;
        int mid=0;
        while(low<=high)
        {
            mid=(low+high)/2;
            if (arr[mid]<k){
                low=mid+1;
                
            }else if(arr[mid]>k){
                high=mid-1;
            }else{
                return mid;
            }
        }
        return -1;
    }
};