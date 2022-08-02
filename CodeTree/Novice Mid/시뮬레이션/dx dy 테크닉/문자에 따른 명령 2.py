dir_num = 3 #북쪽을 바라보고 있음
x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]


commands = input() #ex : "LF"

for command in commands:
    if command == "L": #왼쪽으로 90도 방향 전환
        # rotate direction
        dir_num = (dir_num - 1 + 4) % 4
    elif command == "R": #오른쪽으로 90도 방향 전환
        # rotate direction
        dir_num = (dir_num + 1) % 4
    else: # "F" #바라보고 있는 방향으로 한칸 이동
        # move
         x, y = x + dx[dir_num], y + dy[dir_num]
print(x,y)
