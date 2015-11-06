"""
Given a n,m which means the row and column of the 2D matrix and an array of pair A( size k). Originally, the 2D matrix is all 0 which means there is only sea in the matrix. The list pair has k operator and each operator has two integer A[i].x, A[i].y means that you can change the grid matrix[A[i].x][A[i].y] from sea to island. 
Return how many island are there in the matrix after each operator.

Example
Given n = 3, m = 3, array of pair A = [(0,0),(0,1),(2,2),(2,1)].

return [1,1,2,2].
"""

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
class union_find:
    def __init__(self, m, n):
        self.father = {}
        self.m = m
        self.n = n
        for i in range(m):
            for j in range(n):
                id = self.convert_to_id(i, j)
                self.father[id] = id
    
    def find(self, x, y):
        parent = self.father[self.convert_to_id(x, y)]
        while parent != self.father[parent]:
            parent = self.father[parent]
        return parent
    
    def compressed_find(self, x, y):
        parent = self.father[self.convert_to_id(x, y)]
        while parent != self.father[parent]:
            parent = self.father[parent]
        # set all father to be parent we just get
        prev_father = self.father[self.convert_to_id(x, y)]
        while prev_father != self.father[prev_father]:
            prev_father, self.father[prev_father] = self.father[prev_father], parent
        return parent
    
    def union(self, x1, y1, x2, y2):
        f1 = self.find(x1, y1)
        f2 = self.find(x2, y2)
        if f1 != f2:
            self.father[f1] = f2
    
    def convert_to_id(self, x, y):
        return x * self.n + y
        
class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Pint[]} operators an array of point
    # @return {int[]} an integer array
    def numIslands2(self, n, m, operators):
        # Write your code here
        if m == 0 or n == 0:
            return []
        if not operators or len(operators) == 0:
            return []
        island = [[False for _ in range(m)] for _ in range(n)]
        directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
        count, uf, result = 0, union_find(n, m), []
        for operator in operators:
            count += 1
            x, y = operator.x, operator.y
            if not island[x][y]:
                island[x][y] = True
                for i in range(4):
                    nx, ny = x + directions[i][0], y + directions[i][1]
                    if 0 <= nx < n and 0 <= ny < m and island[nx][ny]:
                        operator_father = uf.find(x, y)
                        now_father = uf.find(nx, ny)
                        if operator_father != now_father:
                            count -= 1
                            uf.union(x, y, nx, ny)
            result.append(count)
        return result
