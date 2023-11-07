class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int max_alt = 0;
        int alt = 0;
        for(int i = 0; i<gain.size();i++){
            alt += gain[i];
            if(alt > max_alt)
                max_alt = alt;
        }
        return max_alt;
    }
};