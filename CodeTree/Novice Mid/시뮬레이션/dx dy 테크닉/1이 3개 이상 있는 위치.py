
'''
상하좌우로 인접한 칸 중 숫자 1이 적혀 있는 칸의 수가 3개 이상인 곳의 개수를 세는 프로그램
'''
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
# (x,y) 위치 기준으로 인접한 칸에 있는 숫자 1의 개수 세기
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

result = 0
for x in range(n):
    for y in range(n):
        dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] == 1:
                cnt += 1
        #인접한 칸에 있는 1의 개수        
        if cnt >= 3:
            result += 1



print(result)
