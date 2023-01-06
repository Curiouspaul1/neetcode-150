#include<vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums){
        std::vector<std::vector<int>> result;

        std::sort(nums.begin(), nums.end());

        int numSize = nums.size();
        int prevKey = INT_MAX;

        for(int i = 0; i < numSize; ++i){        
            int l = i+1;
            int r = nums.size()-1;
            if(prevKey == nums[i]){
                continue;
            }

            while(r > l){
                if(nums[i] + nums[l] + nums[r] > 0){
                    --r;
                }
                else if (nums[i] + nums[l] + nums[r] < 0){
                    ++l;
                }
                else{
                    result.push_back({nums[i],nums[l],nums[r]});
                    ++l;
                    while(nums[l] == nums[l-1] && l < r){
                        ++l;
                    }
                }
            }
            prevKey = nums[i];
        }
        return result;
    }
};