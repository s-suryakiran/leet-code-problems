class Solution
{
public:
    vector<int> mostVisited(int n, vector<int> &rounds)
    {
        vector<int> count(n);
        int s = rounds[0] - 1;
        count[s]++;
        for (int i = 0; i < rounds.size(); i++)
        {
            while (s != rounds[i] - 1)
            {
                s++;
                s %= n;
                count[s]++;
            }
        }
        int maxi = *max_element(count.begin(), count.end());
        vector<int> ans;
        for (int i = 0; i < count.size(); i++)
        {
            if (count[i] == maxi)
            {
                ans.push_back(i + 1);
            }
        }
        return ans;
    }
};