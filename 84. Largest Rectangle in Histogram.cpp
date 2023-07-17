class Solution
{
public:
    int largestRectangleArea(vector<int> &heights)
    {

        stack<tuple<int, int>> s;
        int li, lh;
        int maxarea = 0;
        for (int i = 0; i < heights.size(); i++)
        {
            li = i;
            while (!s.empty() && heights[i] < get<1>(s.top()))
            {
                li = get<0>(s.top());
                lh = get<1>(s.top());
                int area = lh * (i - li);
                maxarea = max(area, maxarea);
                s.pop();
            }
            s.push(tuple(li, heights[i]));
        }
        while (!s.empty())
        {
            int area = (heights.size() - get<0>(s.top())) * get<1>(s.top());

            maxarea = max(maxarea, area);
            s.pop();
        }
        return maxarea;
    }
};