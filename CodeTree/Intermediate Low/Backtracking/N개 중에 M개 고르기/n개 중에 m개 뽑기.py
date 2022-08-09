n, m = map(int, input().split())
combination = []

def print_combination():
    for elem in combination:
        print(elem, end = " ")
    
    print()

def find_combination(current, count):
    if current == n + 1: #n개의 숫자 모두 탐색
        if count == m: #m개의 숫자를 뽑음
            print_combination()
        return

    combination.append(current)
    #current에 해당하는 숫자를 사용
    find_combination(current + 1, count + 1)
    combination.pop()
    #current에 해당하는 숫자를 사용하지 않음
    find_combination(current + 1, count)

find_combination(1, 0)
