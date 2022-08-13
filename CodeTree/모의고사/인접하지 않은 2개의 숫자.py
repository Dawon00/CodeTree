n = int(input())
num_list = list(map(int, input().split()))
valid = []
max_sum = 0
_sum = 0
for i in range(n):
    for j in range(n):
        if j != i+1 and j != i-1 and j != i: 
            valid.append(num_list[j])
    for k in range(len(valid)):
        _sum = num_list[i] + valid[k]
        if _sum >  max_sum:
            max_sum = _sum
    valid = []

print(max_sum)
