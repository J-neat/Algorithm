import sys
sys.stdin = open('10773.txt', 'r')

howmany = int(input())

stack = []
sum = 0
for i in range(howmany):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

for j in range(len(stack)):
    sum += stack[j]

print(sum)