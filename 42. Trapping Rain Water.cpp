class Solution
{
public:
    int trap(vector<int> &height)
    {
        int l = 0;
        int r = height.size() - 1;
        int maxLeft = height[l];
        int maxRight = height[r];
        int ans = 0;
        while (l < r)
        {
            if (maxLeft <= maxRight)
            {
                l++;
                ans = ans + max(0, (maxLeft - height[l]));
                maxLeft = max(maxLeft, height[l]);
            }
            else
            {
                r--;
                ans = ans + max(0, (maxRight - height[r]));
                maxRight = max(maxRight, height[r]);
            }
        }
        return ans;
    }
};