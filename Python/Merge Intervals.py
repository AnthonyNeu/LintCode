"""
Given a collection of intervals, merge all overlapping intervals.

Example
Given intervals => merged intervals:

[                     [
  [1, 3],               [1, 6],
  [2, 6],      =>       [8, 10],
  [8, 10],              [15, 18]
  [15, 18]            ]
]
Challenge
O(n log n) time and O(1) extra space.
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # write your code here
        if not intervals:
            return intervals
        intervals.sort(key = lambda x : x.start)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            prev, cur = result[-1], intervals[i]
            if prev.end >= cur.start:
                prev.end = max(cur.end, prev.end)
            else:
                result.append(cur)
        return result
