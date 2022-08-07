# 변수 선언 및 입력
n, curr_x, curr_y = tuple(map(int, input().split()))
a = [[0] * (n + 1)]
for _ in range(n):
    a.append([0] + list(map(int, input().split())))

# 방문하게 되는 숫자들을 담을 곳.
visited_nums = []


# 범위가 격자 안에 들어가는지 확인
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 범위가 격자 안이고, 해당 위치의 값이 더 큰지 확인
def can_go(x, y, curr_num):
    return in_range(x, y) and a[x][y] > curr_num



def simulate():
    global curr_x, curr_y
    
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    # 나아갈수있는지 확인
    for dx, dy in zip(dxs, dys):
        next_x, next_y = curr_x + dx, curr_y + dy
        
        # 갈 수 있는 곳이라면 이동
        if can_go(next_x, next_y, a[curr_x][curr_y]):
            curr_x, curr_y = next_x, next_y
            return True
    
    # 움직일 곳이 없음
    return False


# 초기 위치에 적혀있는 값을 답에 넣어줍니다.
visited_nums.append(a[curr_x][curr_y])
while True:
    # 움직이기
    greater_number_exist = simulate()
    
    # 인접한 곳에 더 큰 숫자가 없다면 종료
    if not greater_number_exist:
        break
    
    # 움직이고 난 후의 위치를 답에 넣어줍니다.
    visited_nums.append(a[curr_x][curr_y])

# 출력:
for num in visited_nums:
    print(num, end=' ')
