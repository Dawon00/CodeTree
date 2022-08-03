n = int(input())
dxs, dys = [1,0,-1,0], [0,-1,0,1]
x, y = 0, 0
time = 0;
flag = 'fail'

for _ in range(n):
    direction, distance = map(str, input().split()) #이동 방향과 거리를 n번 입력받음
    distance = int(distance)

    if direction == 'N':
        dir_num = 3
    elif direction == 'E':
        dir_num = 0
    elif direction == 'S':
        dir_num = 1
    else:
        dir_num = 2

    for _ in range(distance): #거리만큼 앞으로 나아감
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        x, y = x + dxs[dir_num], y + dys[dir_num]
        time += 1
        if nx == 0 and ny == 0: #시작점인 0,0 으로 돌아오면
            print(time)
            flag = 'success'
            break
    if flag == 'success':
        break

if flag == 'fail': #시작점으로 돌아오지 못하면
    print('-1')
