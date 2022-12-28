#include<iostream>
#include<vector>
#include<map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> indexMap; 
        int complement = 0;
        int i = 0;

        for(; i < nums.size(); ++i){
            complement = target - nums[i];
            if(indexMap.count(complement) == 1)
                break;
            else
                indexMap[nums[i]] = i;
        }

        return {i, indexMap[complement]};
    }
};