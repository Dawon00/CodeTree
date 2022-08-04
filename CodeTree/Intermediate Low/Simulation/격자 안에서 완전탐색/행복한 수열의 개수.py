# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
seq = [0 for _ in range(n)]




num_happy = 0

# 먼저 가로로 행복한 수열의 수를 셉니다.
for i in range(n): #한줄 씩
    seq = grid[i][:]

     # 주어진 seq가 행복한 수열인지 판단
    count, max_ccnt = 1, 1
    for i in range(1, n):
        if seq[i - 1] == seq[i]:
            count += 1
        else:
            count = 1
        
        max_ccnt = max(max_ccnt, count)
    
    # 최대로 연속한 회수가 m이상이면 true를 반환합니다. 
    if max_ccnt >= m :
        num_happy += 1

# 세로로 행복한 수열의 수를 셉니다.
for j in range(n): #한줄 씩
    # 세로로 숫자들을 모아 새로운 수열을 만듭니다.
    for i in range(n):
        seq[i] = grid[i][j]
    
     # 주어진 seq가 행복한 수열인지 판단
    count, max_ccnt = 1, 1
    for i in range(1, n):
        if seq[i - 1] == seq[i]:
            count += 1
        else:
            count = 1
        
        max_ccnt = max(max_ccnt, count)
    
    # 최대로 연속한 회수가 m이상이면 true를 반환합니다. 
    if max_ccnt >= m :
        num_happy += 1

print(num_happy)
