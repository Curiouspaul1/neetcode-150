#include<algorithm>
#include<string>
#include<vector>
#include<map>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<string> temp (strs);
        map<string, vector<string>> hashMap;
        vector<vector<string>> result;

        for(int i = 0; i < strs.size(); ++i){
            sort(strs[i].begin(), strs[i].end());
        }

        for(int i = 0; i < strs.size(); ++i){
            hashMap[strs[i]].push_back(temp[i]);
        }
        for(map<string, vector<string>>::iterator  it = hashMap.begin(); it != hashMap.end(); ++it){
            result.push_back(it->second);
        }

        return result;
                
    }
};