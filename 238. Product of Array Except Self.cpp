class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int arraylength = nums.size();
        vector<int> pre(arraylength);
        vector<int> post(arraylength);
        vector<int> ans(arraylength);
        pre[0] =1;
        post[arraylength-1] = 1;
        for (int i = 1;i<arraylength;i++){
            pre[i] = nums[i-1]*pre[i-1];
        }
        for(int i =arraylength-2; i>=0; i--){
            post[i] = nums[i+1] * post[i+1];
        }

        for(int i =0 ; i<arraylength;i++){
            ans[i] = pre[i] * post[i];
        }
        return ans;
    }
};