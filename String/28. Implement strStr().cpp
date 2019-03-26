/*
* Implement strStr().
* Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
*/
class Solution {
public:
    int strStr(string s1, string s2) {
        int m = s1.length(); 
        int n = s2.length(); 
        for (int i = 0; i <= m - n; ++i) { 
        int j; 
        for (j = 0; j < N; ++j) 
            if (s1[i + j] != s2[j]) 
                break; 
  
        if (j == N) 
            return i; 
        } 
        return -1;
    }
};