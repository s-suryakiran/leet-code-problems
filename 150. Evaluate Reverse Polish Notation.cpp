#include <stack>
#include <string>
using namespace std;
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;
        string token;
        for(string i : tokens){
            token = i;
            if(token == "+" ||token == "*" || token == "-" || token == "/")
            {
                int b = s.top();
                s.pop();
                int a = s.top();
                s.pop();
                int c;
                
                if(token == "+")
                    c = a+b;
                    
                else if(token == "-")
                    c = a-b;
        
                else if(token == "*")
                    c = a*b;
                
                else if(token =="/")
                    c = a/b;

            
                s.push(c);
            }
            else{
                int d = stoi(token);
                s.push(d);
            }
        }
    int ans = s.top();
    s.pop();
    return ans;
    }
};