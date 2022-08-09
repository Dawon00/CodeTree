k, n = map(int, input().split())
num_list = []

def find_permutation(count):
    if count == n: #n개 다 뽑았으면 완성된 숫자 출력
        for num in num_list:
            print(num, end=" ")
        print()
        return
    for i in range(1, k+1): #1부터 k까지 뽑기
        num_list.append(i)
        find_permutation(count + 1)
        num_list.pop()

find_permutation(0)
