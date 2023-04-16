#include <stack>
using namespace std;
class MinStack {
public:
stack<int> min_stack;
stack<int> value_stack;
    MinStack() {
        stack<int> min_stack;
        stack<int> value_stack;
    }
    
    void push(int val) {
        if (this->value_stack.empty()){
            this->min_stack.push(val);
            this->value_stack.push(val);
        }
        else{
            if (this->min_stack.top()>val){
                this->min_stack.push(val);
                this->value_stack.push(val);
            }
            else{
                this->min_stack.push(this->min_stack.top());
                this->value_stack.push(val);
            }
        }
    }
    
    void pop() {
        this->min_stack.pop();
        this->value_stack.pop();
    }
    
    int top() {
        return value_stack.top();
        
    }
    
    int getMin() {
        return min_stack.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */