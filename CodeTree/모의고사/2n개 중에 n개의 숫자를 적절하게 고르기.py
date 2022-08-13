from itertools import combinations
import copy

n = int(input())
num_list = list(map(int, input().split()))
min_dif = float("inf")
list_1 = list(combinations(num_list, n))
num_list_copy = list(num_list)

for i in range(len(list_1)):
    list_2 =[]
    num_list_copy = list(num_list)
    for j in range(n):
        if list_1[i][j] in num_list_copy:
           num_list_copy.remove(list_1[i][j])
    list_2 = num_list_copy
    sum_1 = sum(list_1[i])
    sum_2 = sum(list_2)

    if abs(sum_1 - sum_2)  < min_dif:
        min_dif = abs(sum_1 - sum_2)
    
print(min_dif)
