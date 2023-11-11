class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        int cnt=0;
        unordered_map<int,int> m;
        for(int i = 0 ;i< nums.size();i++){
            if(m[k - nums[i]] > 0){
                m[k - nums[i]]--;
                cnt++;
            }
            else{
                m[nums[i]]++;
            }
        }
        return cnt;

    }
};