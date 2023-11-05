class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int max_sum = 0;
        int sum = 0;
        for (int i = 0;i<k;i++){
            max_sum += nums[i];
        }
        sum = max_sum;

        int si =0;
        int ei = k;
        while(ei < nums.size()){
            sum += nums[ei];
            sum -= nums[si];
            ei++;
            si++;

            if(sum > max_sum){
                max_sum = sum;
            }
        }

        return double(max_sum)/double(k);
    }
};