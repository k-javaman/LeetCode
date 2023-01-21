class Solution {
    public void reverseString(char[] s) {
        // create two pointers
        int lo = 0;
        int hi = s.length - 1;
        // swap
        while(lo < hi) {
            char tmp = s[lo];
            s[lo] = s[hi];
            s[hi] = tmp;
            lo++;
            hi--;
        }
    }
}