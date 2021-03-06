"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
"""

class Solution:
    def getRow(self, rowIndex):
        res = []
        for i in range(rowIndex + 1):
            res.append([])
            for j in range(i + 1):
                if j in(0, i):
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1] + res[i-1][j])
                    
        return res[rowIndex]

print(Solution().getRow(5))
        

