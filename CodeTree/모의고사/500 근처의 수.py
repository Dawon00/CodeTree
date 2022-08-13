num_list = list(map(int, input().split()))
max_num = 1
min_num = 1000
for num in num_list:
    if num < 500:
        if num > max_num:
            max_num = num
    if num > 500:
        if num < min_num:
            min_num = num

print(max_num, min_num)
