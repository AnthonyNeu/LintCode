"""

"""

class Solution:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def maxPoints(self, points):
        # Write your code here
        n, result = len(points), 0
        dic = {}
        for i in range(n):
            dic.clear()
            """
            ss is the number of points with same slope
            sp is the number of same point
            """
            ss, sp = 1, 0
            for j in range(i + 1, n):
                slope = float('inf')
                if points[i].x != points[j].x:
                    slope = 1.0 * (points[j].y - points[i].y) / (points[j].x - points[i].x)
                elif points[i].y == points[j].y:
                    sp += 1
                    continue
                if slope in dic:
                    dic[slope] += 1
                    ss = max(ss, dic[slope])
                else:
                    dic[slope] = 2
                    ss = max(ss, 2)
            result = max(result, ss + sp)
        return result

# a solution using GCD to represent the slope of a line to avoid using float number in hash table.
class MyPoint:
    def __init__(self, x, y):
        g = self.gcd(abs(x), abs(y))
        if x == 0 and y == 0:
            self.dx, self.dy = 0, 0
        elif x == 0:
            self.dx, self.dy = 0, 1
        elif y == 0:
            self.dx, self.dy = 1, 0
        elif y > 0:
            self.dx, self.dy = x / g, y / g
        elif y < 0:
            self.dx, self.dy = - x / g, - y / g

    def gcd(self, a, b):
        """
        calculate gcd of a and b
        """
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def __eq__(self, other):
        return other.dx == self.dx and other.dy == self.dy

    def __hash__(self):
      return hash((self.dx, self.dy))

class Solution:
    # @param {int[]} points an array of point
    # @return {int} an integer
    def maxPoints(self, points):
        # Write your code here
        from collections import defaultdict
        n, result = len(points), 0
        dic, zero = defaultdict(int), MyPoint(0, 0)
        for i in range(n):
            dic.clear()
            ss, sp = 1, 0
            for j in range(i + 1, n):
                slope = MyPoint(points[i].x - points[j].x, points[i].y - points[j].y)
                if slope == zero:
                    sp += 1
                elif slope in dic:
                    dic[slope] += 1
                    ss = max(ss, dic[slope])
                elif slope not in dic:
                    dic[slope] = 2
                    ss = max(ss, 2)
            result = max(result, ss + sp)
        return result
