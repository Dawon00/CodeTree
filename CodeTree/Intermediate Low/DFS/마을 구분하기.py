n = int(input()) # n*n
people = 0
people_list = []

grid = [
    list(map(int, input().split()))
    for _ in range(n)
] #그리드 만들기

visited = [
    [0 for _ in range(n)]
    for _ in range(n)
] #방문했는지

def in_range(x, y): #범위 벗어나는지
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x, y):
    if not in_range(x,y):
        return False

    if visited[x][y] or grid[x][y] == 0:
        return False
    return True

def dfs(x, y):
    global people
    # 0 오른쪽 1 아래쪽 2 왼쪽 3 위쪽
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        
        if can_go(new_x, new_y):
            visited[new_x][new_y] = 1
            people += 1
            dfs(new_x, new_y)

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            visited[i][j] = True #방문한걸로 처리하기
            people = 1 #사람 수 1로 리셋
            dfs(i, j) #마을 사람 수 세기
            people_list.append(people) #다 세면 리스트에 추가하기

people_list.sort() #마을사람 수 오름 차순으로 정렬하기
print(len(people_list))
for x in people_list:
    print(x)
