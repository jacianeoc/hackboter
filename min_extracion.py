t = int(input())
 
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    lst = list()
 
    if n == 1:
        print(*arr)
        continue
 
    while len(arr) > 1:
        m = min(arr)
        arr.remove(m)
        arr = list(map(lambda x: x - m, arr))
        lst.append(m)
 
    lst.append(arr[0])
    print(max(lst))
