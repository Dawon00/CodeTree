n=int(input())
x, y = 0,0
for _ in range(n):
    c_dir, dist = tuple(input().split()) # "N" , "3"
    dist = int(dist)

    dir_num = 0
    dx = [1,0,-1,0]
    dy = [0,-1,0,1]

    if c_dir == "N":
        dir_num = 3
    elif c_dir == "E":
        dir_num = 0
    elif c_dir == "S":
        dir_num = 1
    else:
        dir_num = 2

    x = x + dx[dir_num] * dist
    y = y + dy[dir_num] * dist

print(x, y)
