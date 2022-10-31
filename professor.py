def solve():
    start = [int(i) for i in input().split()]
    end = [int(i) for i in input().split()]
 
    diff_x = abs(start[0] - end[0])
    diff_y = abs(start[1] - end[1])
 
    if diff_x == diff_y:
        print(diff_x)
    else:
        print((max(diff_x, diff_y) - min(diff_x, diff_y)) + min(diff_x, diff_y))
 
 
solve()
