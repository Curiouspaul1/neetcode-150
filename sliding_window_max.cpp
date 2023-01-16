class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {

        priority_queue<int>pq;
        unordered_map<int,int>mp;
        vector<int>ans;
        int n = nums.size();
        for(int i=0;i<k;++i)
        {
            pq.push(nums[i]);
        }
        int t = pq.top();
        ans.push_back(t);
        int l = 1;
        int r = k;
        while(r<n)
        {
            // Add the new right guy into the heap
            pq.push(nums[r]);
            // gotta remove l-1 guy from heap
            mp[nums[l-1]]++;
            int tt = pq.top();
            while(pq.size() and mp.find(tt)!=mp.end())
            {
                mp[tt]--;

                if(mp[tt]==0)
                {
                    mp.erase(tt);
                }
                pq.pop();
                tt = pq.top();
            }
            ans.push_back(pq.top());
            r++;
            l++;
        }
        return ans;


        
    }
};
