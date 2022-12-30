#include<vector>
#include<map>

using namespace std;


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int>freqTable;
        map<int, vector<int>>revFreqTable;
        vector<int>result;

        for(auto i : nums){
            ++freqTable[i];
        }

        for(auto i = freqTable.begin(); i != freqTable.end(); ++i){
            revFreqTable[i->second].push_back(i->first);
        }

        auto j = revFreqTable.end();
        --j;
        int i = 0;
        while(i < k){
            result.insert(result.end(), j->second.begin(), j->second.end());
            i += j->second.size();
            --j;
        }

        return result;
        
    }
};