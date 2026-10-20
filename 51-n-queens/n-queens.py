class Solution(object):
    def solveNQueens(self, n):
        res, cols, l_diag, r_diag = [], set(), set(), set()
        def dfs(r, pos): 
            if r == n:
                res.append(['.' * i + 'Q' + '.' * (n - i - 1) for i in pos])
                return
            for c in range(n):
                if not c in cols and not r - c in l_diag and not r + c in r_diag:
                    cols.add(c)
                    l_diag.add(r - c)
                    r_diag.add(r + c)
                    dfs(r + 1, pos + [c])
                    cols.remove(c)
                    l_diag.remove(r - c)
                    r_diag.remove(r + c)
            
        dfs(0, [])
        return res