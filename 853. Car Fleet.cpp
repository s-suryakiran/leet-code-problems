class Solution
{
public:
    int carFleet(int target, vector<int> &position, vector<int> &speed)
    {
        stack<float> time;
        vector<tuple<int, int>> pair;
        for (int i = 0; i < position.size(); i++)
        {
            pair.push_back(tuple(position[i], speed[i]));
        }
        sort(pair.begin(), pair.end());
        float t = (target - get<0>(pair[pair.size() - 1])) / (float)get<1>(pair[pair.size() - 1]);
        time.push(t);
        for (int i = pair.size() - 2; i >= 0; i--)
        {
            t = (target - get<0>(pair[i])) / (float)get<1>(pair[i]);
            if (time.top() < t)
            {
                time.push(t);
            }
        }

        return time.size();
    }
};