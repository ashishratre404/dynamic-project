    for r in range(rows - 1, -1,-1):
        for c in range(cols -1, -1,-1):
            res[r][c] = grid[r][c] + min(res[r+1][c], res[r][c+1])
        return res[0][0]