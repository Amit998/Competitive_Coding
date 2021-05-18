#include<vector>
#include<iostream>

using namespace std;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left=binSearch(nums,target);
        int right=binSearch(nums,target+1)-1;
        if(left <=right){
            return {left,right};
        }

        return {-1,-1};
        
    }
public:
    int binSearch(vector<int>& nums, int target){
        int n=nums.size();
        int first_pos=n;
        int low = 0,high = n-1;

        while(low <= high){
            int mid=low+(high-low)/2;
            if  (nums[mid] >=target){
                first_pos=mid;
                high = mid-1;

            }else{
                low = mid+1;
            }
        }
        return first_pos;

    };
};

int main(){
    Solution s;

    int target;
    vector<int> nums;




    s.searchRange(nums,target);


    return 0;
}
