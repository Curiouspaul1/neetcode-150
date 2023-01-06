class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::set<int> numsSet(nums.begin(), nums.end());
        std::vector<int> answer;

        for(int i = 0; i < nums.size(); i++) {
            int temp = target - nums[i];
            if(auto search = numsSet.find(temp); search != numsSet.end()) {
                auto tempIdx = std::find(nums.begin(), nums.end(), temp);
                int index = tempIdx - nums.begin();
                if(index != i) {
                    answer.push_back(i);
                    answer.push_back(index);
                    break;
                }
            }
        }
        return answer;
    }
};
