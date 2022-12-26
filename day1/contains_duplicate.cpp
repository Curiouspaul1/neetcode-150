#include<iostream>
#include<vector>
#include<map>


class Solution {
public:
    bool containsDuplicate(std::vector<int>& nums) {
        std::map<int, int> valueCount;
        bool result = false;
        for(int i : nums){
            //checking if value is in the map already
            if(valueCount.find(i) != valueCount.end()){
                result = true;
                break;
            }
            else{
                ++valueCount[i]; 
            }
        }

        return result;         
    }
};