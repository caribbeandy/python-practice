from typing import List

# TODO TRY TO PRINT OUTSIDE OF THE MATRIX
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        if m == 0:
            return res
        n = len(matrix[0])

        if n ==0:
            return res

        for i in range(m):
            for j in range(n):
                print(matrix[i][j], end="\t")
            print()

        print()

        i=0
        j=0

        while i<=m and j<=n:

            for a in range(j,n-1):
                res.append(matrix[i][a])

            res.append("x")
            for a in range(i,m-1):
                res.append(matrix[a][n-1])

            if i!=m-1:
                res.append("x")
                for a in range(n-1,j,-1):
                    res.append(matrix[m-1][a])

            if j!=n-1:
                res.append("x")
                for a in range(m-1,i,-1):
                    res.append(matrix[a][j])

            i+=1
            j+=1
            m-=1
            n-=1


        return res


res = Solution().spiralOrder([[0, 1, 2], [3, 4, 5], [6,7,8], [9,10,11]])
#assert res == [0, 1, 2, 5, 8, 11, 10, 9, 6, 3, 4, 7]
print(res)
print()


res = Solution().spiralOrder([[]])
#assert res == []
print(res)
print()


res = Solution().spiralOrder([[1,2,3]])
print(res)
print()
