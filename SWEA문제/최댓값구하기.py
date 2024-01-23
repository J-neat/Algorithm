import sys

sys.stdin = open('../input.txt', 'r')

Data = [list(map(int, input().split())) for i in range(100)]

max_sum = 0

for i in range(100):
    row_sum = sum(Data[i])
    max_sum = max(max_sum, row_sum)

    col_sum = sum(Data[i][j] for j in range(100))
    max_sum = max(max_sum, col_sum)

diag_sum = sum(Data[i][i] for i in range(100))
max_sum = max(max_sum, diag_sum)


print(max_sum)
