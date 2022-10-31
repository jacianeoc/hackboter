import sys
input = sys.stdin.readline
from collections import Counter as C
def miis():
    return map(int, input().split())
 
for _ in range(1):
    n = int(input())
    a = list(miis())
    c = C(a)
    ans = n-1
    for i in c:
        ans = min(n-c[i], ans)
    print(ans)
