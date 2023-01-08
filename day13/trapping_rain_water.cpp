#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        vector<int>maxLeft;
        vector<int>maxRight(height.size());
        int max = 0;
        int result = 0;

        maxLeft.push_back(0);
        for(int i = 1; i < height.size(); ++i){
            max = std::max(max, height[i-1]);
            maxLeft.push_back(max);
        }

        maxRight[height.size()-1] = 0;
        max = 0;
        for(int i = height.size()-2; i >= 0; --i){
            max = std::max(max, height[i+1]);
            maxRight[i] = max;
        }

        int unitTrap = 0;
        for(int i = 0; i < height.size(); ++i){
            unitTrap = min(maxLeft[i], maxRight[i]) - height[i];
            unitTrap > 0 ? result+=unitTrap : result+=0; 
        }

        return result;
        
    }
};