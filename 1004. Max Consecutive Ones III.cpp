class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int start = 0;
        int max_count = 0;
        for (int i = 0 ;i< nums.size();i++){
            if(nums[i] == 0){
                k--;
            }
            if (k < 0){
                if(nums[start] == 0)
                    k++;
                start++;
            }
            if(max_count < i-start+1)
                max_count = i - start + 1;
        }
        return max_count;
    }
};