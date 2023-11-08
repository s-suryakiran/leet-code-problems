class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        map<int,int> m;
        set<int> s;
        for(int i = 0 ; i < arr.size(); i++){
            m[arr[i]] ++;
        }
        for(auto in: m){
            if(s.count(in.second) == 0){
                s.insert(in.second);
            }
            else{
                return false;
            }
        }
        return true;
    }
};