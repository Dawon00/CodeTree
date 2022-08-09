k, n = map(int, input().split())

num_list = []

def find_duplicated_permutation(count):
    #n개 뽑으면 출력
    if count == n:
        for num in num_list:
            print(num, end=" ")
        print()
        return
    for i in range(1, k+1):
        if count >= 2 and i == num_list[-1] and i == num_list[-2]:
            continue
        else:
            num_list.append(i) #숫자 추가하고
            find_duplicated_permutation(count + 1) #중복확인하고
            num_list.pop() #숫자 다시 지우기
find_duplicated_permutation(0)
