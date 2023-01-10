#include<map>
#include<string>
#include<iostream>

using namespace std;

int characterReplacement(string s, int k){
    std::ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    map<char, int> charFreq;
    int max = 0, n = s.size(), l = 0, r = 0, longestSubstring = 0;

    //cout << ++charFreq['A'] << " " << ++charFreq['A'];

    while(r < n){
        //cout << s[r] << "";
        ++charFreq[s[r]];
        //update max if the current character is the most frequent
        max = charFreq[s[r]] > max ? charFreq[s[r]] : max;
        // cout << max << endl;
        int replaceableCharacter = (r-l+1) - max;
        if(replaceableCharacter <= k){
            longestSubstring = (r-l+1 > longestSubstring) ? r-l+1 : longestSubstring;
            ++r;
        }
        else{
            --charFreq[s[l]];
            ++l;
            ++r;
        }
        
    }

    return longestSubstring;

}

int main(){
    string test = "ABAB";
    int k = 2;
    cout << characterReplacement(test, k);
}