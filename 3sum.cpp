#include <vector>
#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {

        sort(nums.begin(),nums.end());

        vector<vector<int>> res;


        for (int i=0;i<(int)nums.size()-2;i++){

            if (i==0 || (i> 0 && nums[i] !=nums[i-1])){

                int lower= i+1, higher= (int) nums.size()-1,sum=0-nums[i];

                while (lower < higher)
                {
                    if(nums[lower] + nums[higher] == sum){
                
                    vector<int> temp;
                    temp.push_back(nums[i]);
                    temp.push_back(nums[lower]);
                    temp.push_back(nums[higher]);
                    res.push_back(temp);
                    while (lower < higher && nums[lower] == nums[lower+1]) lower++;
                    while (lower < higher && nums[higher] == nums[higher-1]) higher--;
                    lower++;higher--;
                }
                else if(nums[lower] + nums[higher] < sum) lower++;
                else higher--;
                }
            }
        }
        return res;
    }
};


int main(){

    Solution sl;
    // sl.threeSum();
    // sl.threeSum();

    return 0;
}
