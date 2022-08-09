#n번의 턴에 대해 k개 중에 어떤말 움직일건지 선택하는 재귀함수
#backtracking으로 어떤말 움직일지 모든 조합 만들어보기 -> 최대 출력하기


n, m, k = map(int, input().split()) #턴, 판, 말의수
nums = list(map(int, input().split())) #주어지는 숫자들
pieces = [1 for _ in range(k)] #말 리스트

result = 0

def find_max(count):
    global result

    result = max(result, calcuation()) #답 갱신

    if count == n: #턴이 끝나면 끝
        return 
    
    for i in range(k): #말이 이미 끝까지 도착하면 그만 움직임.
        if pieces[i] >= m:
            continue
        pieces[i] += nums[count]
        find_max(count + 1)
        pieces[i] -= nums[count]

def calcuation(): #점수를 계산함
    score = 0
    for piece in pieces:
         score += (piece >= m)  
    return score

find_max(0)
print(result)
