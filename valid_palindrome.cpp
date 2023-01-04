class Solution {
public:
    bool isPalindrome(string s) {
       
        s.erase(remove_if(s.begin(), s.end(), [](const char &c){ return !isalnum(c); }), s.end());
       
        transform(s.begin(), s.end(), s.begin(),[](unsigned char c){ return tolower(c); });
       
        int n = s.size();
        int i=0;
        int j=n-1;

        while(i<=j){
            if(s[i]!=s[j]){
                return false;
            }
            i++;
            j--;
        }

        return true;
    }
};
