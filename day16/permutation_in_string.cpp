#include<iostream.
#include<string>

using namespace std;

class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        sort(s1.begin(), s1.end());
        int n = s1.size();
        
        int startWindow = 0;
        int endWindow = 0;
        int count = 1;
        string temp ="";
        bool result = false;
        string temp2 = "";

        while(endWindow < s2.size()){
            if(count == n){
                temp = s2.substr(startWindow, n);
                temp2 = temp;
                sort(temp2.begin(), temp2.end());
                if(temp2 == s1){
                    result = true;
                    break;
                }
                ++startWindow;
                ++endWindow;                        
            }
            if(count != n){
                temp += s2[endWindow];
                ++endWindow;
                ++count;
            }
        }

        return result;
    }
};