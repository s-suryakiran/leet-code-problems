class Solution
{
public:
    int calculate(string s)
    {
        if (s == "")
            return 0;
        vector<int> st;
        int curr = 0;
        char op = '+';
        for (int i = 0; i < s.length(); i++)
        {
            if (isdigit(s[i]))
            {
                curr = curr * 10 + int(s[i] - '0');
            }
            if (!isdigit(s[i]) && s[i] != ' ' || i == s.length() - 1)
            {
                cout << op << endl;
                if (op == '+')
                {
                    st.push_back(curr);
                }
                else if (op == '-')
                {
                    st.push_back(-1 * curr);
                }
                else if (op == '*')
                {
                    int b = st.back();
                    st.pop_back();
                    st.push_back(b * curr);
                }
                else if (op == '/')
                {
                    int b = st.back();
                    st.pop_back();
                    st.push_back(b / curr);
                }
                curr = 0;
                op = s[i];
            }
        }
        int ans = 0;
        for (int i = 0; i < st.size(); i++)
        {
            ans += st[i];
        }
        return ans;
    }
};