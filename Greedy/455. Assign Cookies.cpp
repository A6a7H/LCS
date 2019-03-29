class Solution {
public:
  int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());
        int i = 0, res = 0;
        for (int si : s) {
            if (i == g.size())
                break;
            if (si >= g[i]) {
                ++i;
                ++res;
            }
        }
        return res;
    }
};