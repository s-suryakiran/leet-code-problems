class Solution
{
public:
    vector<int> dailyTemperatures(vector<int> &temperatures)
    {
        stack<tuple<int, int>> s;
        vector<int> ans(temperatures.size(), 0);
        for (int i = 0; i < temperatures.size(); i++)
        {
            while (!s.empty() && get<0>(s.top()) < temperatures[i])
            {
                ans[get<1>(s.top())] = i - get<1>(s.top());
                s.pop();
            }
            s.push(tuple<int, int>(temperatures[i], i));
        }
        return ans;
    }
};