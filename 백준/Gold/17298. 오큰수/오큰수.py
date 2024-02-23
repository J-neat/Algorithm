from collections import deque

howmany = int(input())
num = list(map(int, input().split()))

my_num = [-1] * howmany
stack = deque()

for i in range(howmany):
    while stack and (num[stack[-1]] < num[i]):
        my_num[stack.pop()] = num[i]
    stack.append(i)

for i in my_num:
    print(i, end=' ')
