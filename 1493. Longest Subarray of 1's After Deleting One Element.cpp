class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int k = 1, max_count = 0, start = 0;
        
        for(int i = 0;i< nums.size(); i++)
        {
            if(nums[i] == 0)
             k--;
            if(k < 0){
                if(nums[start] == 0){
                    k++;
                }
                start++;
            }
            if(max_count < i - start ){
                max_count = i-start;
            }
        }
        return max_count;
        
    }
};