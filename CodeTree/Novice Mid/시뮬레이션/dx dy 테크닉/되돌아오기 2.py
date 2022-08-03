command = input() #FFFRFFRFFFRFFFFFF
command_list = list(command)

dxs, dys = [1,0,-1,0], [0,-1,0,1]
x, y = 0, 0 #처음 위치
dir_num = 3 #북쪽을 향한 상태
time = 0 #시간 재기
flag = 0

for i in range(len(command_list)):
    if command[i] == 'F': #앞으로 한칸 이동
        nx = x + dxs[dir_num] #다음칸의 위치
        ny = y + dys[dir_num]

        x = x + dxs[dir_num] #현재 위치 이동
        y = y + dys[dir_num]

        time += 1
        if x == 0 and y == 0:#처음으로 돌아왔다면
            flag = 1 
            print(time)
            break
    elif command[i] == 'L': #반시계 방향 전환
        dir_num = (dir_num + 3) % 4 
        time += 1
    else: #'R' 일경우
        dir_num = (dir_num + 1) % 4
        time += 1

if flag == 0: #N번 이동했는데도 시작점으로 돌아오지 못한경우
    print(-1)
