import sys
sys.stdin = open('../input.txt', 'r')
MyMap = [[0 for _ in range(8)] for __ in range(8)]
Visited = [0]*8
Queue = [0] * 8

V, E = map(int, input().split())

for _ in range(E):
    start, stop = map(int, input().split())
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1

start = 1
Queue.append(start)

while Queue:
    here = Queue.pop(0)
    print(here)
    Visited[here] = True

    for next in range(8):
        if MyMap[here][next] and not Visited[next] and next not in Queue:
            Queue.append(next)

