#include<iostream>
#include<vector>
#include<algorithm>
#include<map>

using namespace std;

int longestConsecutive(vector<int>& nums) {
    map<int, int> numMap;

    for(int i = 0; i < nums.size(); ++i){
        numMap[nums[i]]= i;
    }

    int prev = 0;
    int count = 0;
    int result = 0; //maximum consecutive sequence

    auto it = numMap.begin();
    while(it != numMap.end()){
        if(count == 0 || it->first - prev == 1){
            prev = it->first;
            ++count;
            result = max(result, count);
        }
        else{
            prev = it->first;
            result = max(result, count);
            count = 0;  //reset count
            ++count;
        }
        ++it;
    }

    return result;
}

int main(){
    vector<int> test = {0,3,7,2,5,8,4,6,0,1};

    cout << longestConsecutive(test) << endl;
}