"""
Given an interval list which are flying and landing time of the flight. How many airplanes are on the sky at most?

Example
For interval list [[1,10],[2,3],[5,8],[4,7]], return 3

Note
If landing and flying happens at the same time, we consider landing should happen at first.
"""

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution1:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        # write your code here
        length = len(airplanes)
        start_times = [airplanes[i].start for i in range(length)]
        end_times =  [airplanes[i].end for i in range(length)]
        start_times.sort()
        end_times.sort()
        max_room, avaliable, start_index, end_index = 0, 0, 0, 0
        while start_index < length:
            if start_times[start_index] < end_times[end_index]:
                if avaliable == 0:
                    max_room += 1
                else:
                    avaliable -= 1
                start_index += 1
            else:
                avaliable += 1
                end_index += 1
        return max_room

class Solution2:
    # @param airplanes, a list of Interval
    # @return an integer
    def countOfAirplanes(self, airplanes):
        # write your code here
        if not airplanes:
            return 0
        airplanes.sort(key = lambda x: x.start)
        rooms = []
        heapq.heappush(rooms, airplanes[0].end)
        for i in range(1, len(airplanes)):
            if airplanes[i].start >= rooms[0]:
                heapq.heappushpop(rooms, airplanes[i].end)
            else:
                heapq.heappush(rooms, airplanes[i].end)
        return len(rooms)
