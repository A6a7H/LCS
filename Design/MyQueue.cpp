#include <iostream>
#include <stack>

using namespace std;

template <typename T>
class MyQueue {
public:

    explicit MyQueue() {
        stack_newest = new stack<T>();
        stack_oldest = new stack<T>();
    }
    int size() {
        return stack_oldest->size() + stack_newest->size();
    }
    void add(T value) {
        stack_newest->push(value);
    }
    T top() {
        shiftStacks();
        return stack_oldest->top();
    }
    T remove() {
        shiftStacks();
        auto res = stack_oldest->top();
        stack_oldest->pop();
        return res;
    }
    ~MyQueue() {
        delete stack_oldest;
        delete stack_newest;
    }
private:

    void shiftStacks() {
        if (stack_oldest->empty()) {
            while (!stack_newest->empty()) {
                stack_oldest->push(stack_newest->top());
                stack_newest->pop();
            }
        }
    }

    stack<T>* stack_oldest;
    stack<T> *stack_newest;
};

int main() {
    MyQueue<int> *q = new MyQueue<int>();
    q->add(5);
    q->add(3);
    cout << q->top() << '\n';
    cout << q->remove();
    q->~MyQueue();
    return 0;
}