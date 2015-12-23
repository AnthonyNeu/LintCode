"""
Given a (decimal - e.g. 3.72) number that is passed in as a string, return the binary representation that is passed in as a string. 
If the fractional part of the number can not be represented accurately in binary with at most 32 characters, return ERROR.

Example
For n = "3.72", return "ERROR".

For n = "3.5", return "11.1".
"""

class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    def binaryRepresentation(self, n):
        # write you code here
        if "." not in n:
            return self.parse_integer(n)
        params = n.split(".")
        frac = self.parse_float(params[1])
        if frac == "ERROR":
            return frac
        if frac == "0" or frac == "":
            return self.parse_integer(params[0])
        return self.parse_integer(params[0]) + "." + frac

    def parse_integer(self, n):
        if not n or n == '0':
            return "0"
        result, n = "", int(n)
        while n > 0:
            result = str(n % 2) + result
            n /= 2
        return result

    def parse_float(self, n):
        result, f = "", float("0." + n)
        dic = {}
        while f:
            if len(result) > 32 or f in dic:
                return "ERROR"
            dic[f] = True
            f *= 2
            if f >= 1:
                result += '1'
                f -= 1
            else:
                result += '0'
        return result
