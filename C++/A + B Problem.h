/*
Write a function that add two numbers A and B. You should not use + or any arithmetic operators.
Example
Given a=1 and b=2 return 3

Note
There is no need to read data from standard input stream. Both parameters are given in function aplusb, you job is to calculate the sum and return it.

Challenge
Of course you can just return a + b to get accepted. But Can you challenge not do it like that?

Clarification
Are a and b both 32-bit integers?

Yes.
Can I use bit operation?

Sure you can.
*/

class Solution {
public:
    /*
     * @param a: The first integer
     * @param b: The second integer
     * @return: The sum of a and b
     */
    int aplusb(int a, int b) {
        // write your code here, try to do it without arithmetic operators.
        /*
        Support we want to add 101 and 011.
        iteration 1:
        a = 110
        b = 010
        iteration 2:
        a = 100
        b = 100
        iteration 3:
        a = 000
        b = 1000

        x ^ y is the add operator without considering the carry
        x & y << 1 is the carry
        */
        while (b != 0) {
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }
};
