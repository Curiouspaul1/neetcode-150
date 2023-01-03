class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        vector<int> ans = {};
        vector<int> countArr = {};
        map<int, int> ansMap;
        // int count = 1;
        for (int i = 0; i < nums.size(); i++)
        {
            ansMap[nums[i]]++;
        }

        for(auto it = ansMap.begin(); it != ansMap.end(); it++) {
            countArr.push_back(it->second);
        }

        sort(countArr.begin(), countArr.end());
        reverse(countArr.begin(), countArr.end());

        int j = 0;
        while (ans.size() != k) 
        {
            for(auto it = ansMap.begin(); it != ansMap.end(); it++) {
                if(countArr[j] == it->second && j < k) {
                    ans.push_back(it->first);
                    j++;
                }
            }
        }

        return ans;
    }
};
