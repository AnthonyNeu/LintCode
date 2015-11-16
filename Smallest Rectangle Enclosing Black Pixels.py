"""
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

For example, given the following image:

[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2,
Return 6.
"""

class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        top = self.search(0, x, lambda mid: '1' in image[mid])
        bottom = self.search(x + 1, len(image), lambda mid: '1' not in image[mid])
        left = self.search(0, y, lambda mid: any(image[k][mid] == '1' for k in xrange(top, bottom)))
        right = self.search(y + 1, len(image[0]), lambda mid: all(image[k][mid] == '0' for k in xrange(top, bottom)))
        return (right - left) * (bottom - top)
    
    def search(self, left, right, check):
        while left != right:
            mid = left + (right - left) / 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
