class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int wl1 = word1.length();
        int wl2 = word2.length();
        int i = 0;
        string combined ="";
        while (i < wl1 && i < wl2){
            combined += word1[i];
            combined += word2[i];
            i++;
        }
        while(i<wl1){
            combined += word1[i];
            i++;
        }
        while(i<wl2){
            combined += word2[i];
            i++;
        }
        return combined;
    }
};