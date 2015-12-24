"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example
Given [1, 20, 23, 4, 8], the largest formed number is 8423201.

Note
The result may be very large, so you need to return a string instead of an integer.

Challenge
Do it in O(nlogn) time complexity.
"""

class Solution: 
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        # write your code here
        dic = {i: [] for i in range(10)}
        for n in num:
            e = 0
            while n / 10 ** e >= 10:
                e += 1
            dic[n / 10 ** e].append(n)
        largest = []
        for i in reversed(range(10)):
            num_list = [str(x) for x in dic[i]]
            num_list.sort(cmp=lambda x, y: cmp(y + x, x + y))
            largest += num_list
        result = ''.join(largest)
        return result.lstrip("0") or "0"

class Solution: 
    #@param num: A list of non negative integers
    #@return: A string
    def largestNumber(self, num):
        # write your code here
        num = [str(x) for x in num]
        num.sort(cmp = lambda x, y: cmp(y + x, x + y))
        return ''.join(num).lstrip('0') or '0'
