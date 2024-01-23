import sys
sys.stdin = open('2606.txt', 'r')

# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

howmany = int(input())
pairs = int(input())

MyMap = [[] for _  in range(howmany+1)]


for _ in range(pairs):
    _from, _to = map(int, input().split())  # _from = 1, _to = 2
    MyMap[_from].append(_to)
    MyMap[_to].append(_from)

start = 1 #무조건 1번 컴퓨터에서 시작함

for now in MyMap:
    now.sort()

Visited = [False] * (howmany+1)
Q = []
def DFS(here):
    Q.append(here)
    Visited[here] = True
    for next in MyMap[here]:
        if not Visited[next]:
            DFS(next)
DFS(start)

count = 0
for i in range(howmany+1):
    if i in Q:
        count += 1

print(count-1)#1번 컴퓨터 뺴야함