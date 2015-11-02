"""
Numbers keep coming, return the median of numbers at every time a new number added.

Example
For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3].

For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3].

For numbers coming list: [2, 20, 100], return [2, 2, 20].

Challenge
Total run time in O(nlogn).

Clarification
What's the definition of Median? - Median is the number that in the middle of a sorted array. 
If there are n numbers in a sorted array A, the median is A[(n - 1) / 2]. For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.
"""

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__min_heap = []
        self.__max_heap = []

    def add_num(self, num):
        from heapq import heappush, heappop
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.__max_heap or num > self.__min_heap[0]:
            heappush(self.__min_heap, num)
            if len(self.__min_heap) > len(self.__max_heap) + 1:
                heappush(self.__max_heap, -heappop(self.__min_heap))
        else:
            heappush(self.__max_heap, -num)
            if len(self.__max_heap) > len(self.__min_heap):
                heappush(self.__min_heap, -heappop(self.__max_heap))

    def find_median(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        return -self.__max_heap[0] if len(self.__min_heap) == len(self.__max_heap) \
               else self.__min_heap[0]

class Solution:
    """
    @param nums: A list of integers.
    @return: The median of numbers
    """
    def medianII(self, nums):
        # write your code here
        median_finder = MedianFinder()
        result = []
        for num in nums:
            median_finder.add_num(num)
            result.append(median_finder.find_median())
        return result
