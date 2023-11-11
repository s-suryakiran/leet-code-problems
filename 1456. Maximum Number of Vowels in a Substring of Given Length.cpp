class Solution {
public:
    int maxVowels(string s, int k) {
        bool isVowel[s.length()];
        int v = 0;
        for(int i = 0 ;i< s.length(); i++){
            if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
                isVowel[i] = true;
            else
                isVowel[i] = false;
        }
        for(int i = 0 ;i< k; i++){
            if(isVowel[i])
                v++;
        }
        int mv = v;
        int i = 0, j = k;
        while(j< s.length()){
            if(isVowel[j]){
                v++;
            }
            if(isVowel[i]){
                v--;
            }
            if(v> mv){
                mv = v;
            }
            j++;
            i++;
        }
        return mv;
    }
};