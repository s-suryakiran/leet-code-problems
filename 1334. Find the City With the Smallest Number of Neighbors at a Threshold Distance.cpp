class Solution
{
public:
    int findTheCity(int n, vector<vector<int>> &edges, int distanceThreshold)
    {
        vector<vector<int>> mind(n, vector<int>(n, INT_MAX));
        for (auto it : edges)
        {
            mind[it[0]][it[1]] = it[2];
            mind[it[1]][it[0]] = it[2];
        }
        for (int i = 0; i < n; i++)
        {
            mind[i][i] = 0;
        }
        for (int k = 0; k < n; k++)
        {
            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (mind[i][k] == INT_MAX || mind[k][j] == INT_MAX)
                        continue;
                    mind[i][j] = min(mind[i][j], mind[i][k] + mind[k][j]);
                }
            }
        }

        int cntCity = n;
        int cityNo = -1;
        for (int i = 0; i < n; i++)
        {
            int ct = 0;
            for (int j = 0; j < n; j++)
            {
                if (mind[i][j] <= distanceThreshold)
                {
                    ct++;
                }
            }
            if (ct <= cntCity)
            {
                cntCity = ct;
                cityNo = i;
            }
        }
        return cityNo;
    }
};