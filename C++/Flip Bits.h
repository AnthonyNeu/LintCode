/*
Determine the number of bits required to flip if you want to convert integer n to integer m.

Example
Given n = 31 (11111), m = 14 (01110), return 2.

Note
Both n and m are 32-bit integers.
*/

// Time:  O(logn) = O(32)
// Space: O(1)

class Solution {
public:
    /**
     *@param a, b: Two integer
     *return: An integer
     */
    int bitSwapRequired(int a, int b) {
        int cnt = 0;
        for (int c = a ^ b; c != 0; c &= c - 1) {
            ++cnt;
        }
        return cnt;
    }
};
