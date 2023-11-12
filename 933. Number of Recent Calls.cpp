class RecentCounter {
public:
    queue<int> q;
    RecentCounter() {
         this->q = queue<int>(); 
    }
    
    int ping(int t) {
        this->q.push(t);
        while(this->q.front() < t- 3000){
            this->q.pop();
        }
        return this->q.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */