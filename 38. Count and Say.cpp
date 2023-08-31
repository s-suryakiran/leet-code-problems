#include <string>
class Solution
{
public:
    string countAndSay(int n)
    {
        if (n == 1)
        {
            return "1";
        }
        string say = countAndSay(n - 1);
        char prev = say[0];
        int ct = 1;
        string ans = "";
        if (say.length() == 1)
        {
            return "11";
        }

        for (int i = 1; i < say.length(); i++)
        {
            if (prev == say[i])
            {
                ct++;
            }
            else
            {
                ans = ans + to_string(ct) + prev;
                ct = 1;
                prev = say[i];
            }
        }
        ans += to_string(ct) + prev;
        return ans;
    }
};