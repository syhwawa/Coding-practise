"""Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

class Solution:
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            res.append([])
            for j in range(i+1):
                if j in (0, i):
                    res[i].append(1)
                else:
                    res[i].append(res[i-1][j-1]+ res[i-1][j])
        
        return res
print(Solution().generate(5))