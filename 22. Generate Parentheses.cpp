#include<stack>
#include<deque>
#include<string>

using namespace std;

class Solution {
public:
stack<char> s;

vector<string> ans; 
string ele;
int n;
void helper(int opened, int closed){
        if(opened == n && closed == n ){
            stack<char> dup = s;
            while(!dup.empty()){
                ele = dup.top() +ele;
                dup.pop();
            }
            ans.push_back(ele);
            ele = "";
            return;

            }
            if (opened < n){
                s.push('(');
                helper(opened+1, closed);
                s.pop();
            }
            if (closed < opened){
                s.push(')');
                helper(opened, closed+1);
                s.pop();
            }
        }

    vector<string> generateParenthesis(int no) {
        ele = "";
        n= no;
        helper(0,0);
        return ans;
    }
};