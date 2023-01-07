#include<vector>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int area = INT_MIN;
        int i = 0;
        int j = height.size()-1;
        int minimum = 0;
        while(j > i){
            minimum = min(height[i], height[j]);
            area = max(area, minimum * (j-i));
            if(height[j] > height[i]){
                ++i;
            }
            else {
                --j;
            }
        }

        return area;
    }
};
