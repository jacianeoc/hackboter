def pascal_tri(lim):
    comb = [[0]*(lim+1) for x in range(lim+1)]
    for i in range(1, lim+1):
        for j in range(0, i+1):
            if j == 0 or j == i:
                comb[i][j] = 1
            else:
                comb[i][j] = comb[i-1][j-1] + comb[i-1][j]
    return comb
n, m, t = map(int, input().split())
lim = 5
comb = pascal_tri(lim+1)
res = 0
if n < 4 or m < 1:
    res = 0
else:
    for boy in range(4, n+1):
        girl = t-boy
        if girl >= 1 and girl <= m:
            res += (comb[n][boy] * comb[m][girl])
        else:
           
