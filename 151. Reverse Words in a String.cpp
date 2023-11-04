class Solution {
public:
    string reverseWords(string s) {
        stack<string> st;
        string temps = "";
        string ans = "";
        for(int i = 0;i<s.length();i++){
            if(temps.length()!=0 && (s[i] ==' ')){
                st.push(temps);
                st.push(" ");
                temps = "";
            }
            else if(i == s.length()-1){
                temps+=s[i];
                st.push(temps);
            }
            else if (s[i]!=' '){
                temps+=s[i];
            }
        }
        while (st.top() == " "){
            st.pop();
        }
        while(!st.empty()){
            ans += st.top();
            st.pop();
        }
        return ans;
    }
};