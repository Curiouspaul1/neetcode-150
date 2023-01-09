class Solution {
public:
    int maxProfit(vector<int>& prices) {
//         int curLow = INT_MAX;
//         int result = 0;
        
//         for(int i = 0; i < prices.size(); i++) {
//             result = std::max(result, prices[i] - curLow);
//             curLow = std::min(curLow, prices[i]);
//         }
//         return result;
            int ans = 0;
            for(int i=1, temp=prices[0]; i<prices.size(); i++)
                ans = max(ans, prices[i] - exchange(temp, min(temp, prices[i])));
            return ans;
     }
};