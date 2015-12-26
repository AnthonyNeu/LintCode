"""
Given a non-overlapping interval list which is sorted by start point.

Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).

Insert [2, 5] into [[1,2], [5,9]], we get [[1,9]].

Insert [3, 4] into [[1,2], [5,9]], we get [[1,2], [3,4], [5,9]].
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        return self.merge(intervals + [newInterval])

    def merge(self, intervals):
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

class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        if not intervals:
            return [newInterval]
        i, result = 0, []
        while i < len(intervals) and intervals[i].end < newInterval.start:
            result.append(intervals[i])
            i += 1
        while i < len(intervals) and newInterval.end >= intervals[i].start:
            newInterval.start = min(intervals[i].start, newInterval.start)
            newInterval.end = max(intervals[i].end, newInterval.end)
            i += 1
        result.append(newInterval)
        result.extend(intervals[i:])
        return result
