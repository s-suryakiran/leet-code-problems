class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int max_c = INT_MIN;
        vector<bool> ans(candies.size());
        for (int i = 0;i < candies.size();i++){
            if(max_c < candies[i]){
                max_c = candies[i];
            }
        }
        for (int i = 0;i < candies.size();i++){
            if(max_c <= candies[i]+extraCandies){
                ans[i] = true;
            }
            else{
                 ans[i] = false;
            }
        }
        return ans;
    }
};