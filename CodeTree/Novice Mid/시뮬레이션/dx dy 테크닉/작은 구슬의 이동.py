n, t = tuple(map(int, input().split()))
x, y, direction = tuple(input().split())

mapper = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3,
}

x, y, move_dir = int(x) - 1, int(y) -1, mapper[direction]



def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

for _ in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    # 벽에 부딪히면 방향을 바꿈
    if not in_range(nx, ny):  # check whether position is out of grid
        move_dir = 3 - move_dir # change direction
    # 범위 안에 들어오면 그대로 진행
    else:
        x, y = nx, ny

print(x+1, y+1)
