#include<vector>
#include<algorithm>
using  namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxSP = prices[prices.size()-1];
        int day = prices.size()-2;
        int result = 0;

        while(day >= 0){
            result = max(result, maxSP-prices[day]);    
            maxSP = max(maxSP, prices[day]);
        --day;
        }

        return result;
        
    }
};