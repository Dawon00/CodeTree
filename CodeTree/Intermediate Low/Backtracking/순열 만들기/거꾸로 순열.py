n = int(input())
visited = [False] * (n+1)
picked = []

#count : 지금까지 선택한 개수
def get_permutation(count):
    if count == n:
        for element in picked:
            print(element, end=" ")
        print()

    for i in range(n, 0, -1): #범위 변경
        if visited[i]:
            continue

        visited[i] = True
        picked.append(i)

        get_permutation(count + 1)

        visited[i] = False
        picked.pop()

get_permutation(0)
