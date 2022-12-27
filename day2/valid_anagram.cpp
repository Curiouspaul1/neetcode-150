#include<iostream>
#include<map>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        bool result = true;
        map<char, int> charFrequency;

        if(s.size() == t.size()){
            //Storing frequency of all character
            for(char i : s) { ++charFrequency[i]; }

            for(char i : t){
                if(charFrequency.count(i) && charFrequency[i] > 0) { 
                    --charFrequency[i]; 
                }
                else{
                    result = false;
                    break;
                }
            }
        }
        else { 
            result = false;
        }    

        return result;           
    }
};