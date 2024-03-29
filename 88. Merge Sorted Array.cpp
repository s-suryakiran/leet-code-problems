class Solution
{
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        int final_i = m + n - 1;

        m -= 1;
        n -= 1;

        while (m >= 0 && n >= 0)
        {
            if (nums1[m] > nums2[n])
            {
                nums1[final_i] = nums1[m];
                m--;
            }
            else
            {
                nums1[final_i] = nums2[n];
                n--;
            }
            final_i--;
        }
        while (n >= 0)
        {
            nums1[final_i] = nums2[n];
            n--;
            final_i--;
        }
    }
};