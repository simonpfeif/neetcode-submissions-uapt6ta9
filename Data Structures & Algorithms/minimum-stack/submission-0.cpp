class MinStack {
public:
    stack<int> stk;
    stack<int> minstk;
    MinStack() {}
    
    void push(int val) {
        if (stk.empty()) {
            minstk.push(val);
        }
        else if (minstk.top() > val) {
            minstk.push(val);
        }
        else {
            minstk.push(minstk.top());
        }
        stk.push(val);
    }
    
    void pop() {
        stk.pop();
        minstk.pop();
    }
    
    int top() {
        return stk.top();
    }
    
    int getMin() {
        return minstk.top();
    }
};
