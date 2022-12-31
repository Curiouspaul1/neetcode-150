#include<vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int temp = 1;
        vector<int> result;

        //Calculating the prefix
        result.push_back(temp);
        for(int i = 0; i < nums.size()-1; ++i){
            temp *= nums[i];
            result.push_back(temp);
        }

        temp = 1;
        //Calculating the suffix
        for(int i = nums.size()-2; i >= 0; --i){
            temp *= nums[i+1];
            result[i] *= temp; 
        }

        return result;
    }
};