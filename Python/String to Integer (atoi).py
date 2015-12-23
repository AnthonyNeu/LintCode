"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()
        max_int_prefix, min_int_prefix = 214748364, -214748364
        max_int, min_int = 2147483647, -2147483648
        if not s:
            return 0
        idx, sign = 0, 1
        if s[0] == '-' or s[0] == '+':
            sign = 1 if s[0] == '+' else -1
            idx += 1
        tmp = ''
        while idx < len(s) and s[idx].isdigit():
            tmp += s[idx]
            idx += 1
        if len(tmp) == 0:
            return 0
        result = 0
        for i in range(len(tmp)):
            result = ord(tmp[i]) - ord('0') + result * 10
            if i < len(tmp) - 1 and result > max_int_prefix:
                return max_int if sign == 1 else min_int
            if i == len(tmp) - 2 and result == max_int_prefix and int(tmp[i + 1]) > 7:
                return max_int if sign == 1 else min_int
        return sign * result
