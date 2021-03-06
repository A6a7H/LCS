class Solution {
public:
    double myPow(double x, int n) {
		if (n == 0) return 1;
        if (n < 0) {
            return n & 1 ? 1 / x * myPow(x * x, n / 2) : myPow(x * x, n / 2);
        }
        return n & 1 ? x * myPow(x * x, n / 2) : myPow(x * x, n / 2);
    }
};