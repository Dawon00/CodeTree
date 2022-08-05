n = int(input()) #처음 놓여있는 블럭의 수
num_list = []

for i in range(n): #블럭 입력받아 쌓기
    num = int(input())
    num_list.append(num)

start_1, end_1 = map(int, input().split()) #자를 부분 입력받기(첫번째)
start_2, end_2 = map(int, input().split())  #자를 부분 입력받기(두번째)

start_1 += 1
end_1 += 1
start_2 += 1
end_2 += 1


del num_list[start_1 -2 : end_1 -1]
#print(num_list)
del num_list[start_2 -2  : end_2-1]
#print(num_list)


print(len(num_list))
for i in range(len(num_list)):
    print(num_list[i])
