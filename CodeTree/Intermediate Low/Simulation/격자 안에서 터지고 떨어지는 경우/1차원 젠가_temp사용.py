# 변수 선언 및 입력
n = int(input())
numbers = [
    int(input())
    for _ in range(n)
]
end_of_array = n


def cut_array(start_idx, end_idx):
    global end_of_array, numbers
    
    temp_arr = []
    
    # 구간 외의 부분만 temp 배열에 순서대로 저장.
    for i in range(end_of_array):
        if i < start_idx or i > end_idx:
            temp_arr.append(numbers[i])

    # temp 배열을 다시 numbers 배열로 옮기기.
    end_of_array = len(temp_arr)
    for i in range(end_of_array):    
        numbers[i] = temp_arr[i]


# 두 번에 걸쳐 지우는 과정을 반복.
for _ in range(2):
    s, e = tuple(map(int, input().split()))
    cut_array(s - 1, e - 1)

# 출력:
print(end_of_array)
for i in range(end_of_array):
    print(numbers[i])
