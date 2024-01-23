import sys
sys.stdin = open('1753.txt', 'r')

def getMin():
    min = INF
    whereMin = -1
    for now in range(V+1):
        if not Visited[now] and Distance[now] < min:
            min = Distance[now]
            whereMin = now
    return whereMin

INF = int(1e9)
V, E = map(int, input().split())
Start = int(input()) ## 시작점

# print(V, E, Start)
MyMap = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    u, v, w = list(map(int, input().split()))
    MyMap[u][v] = w

# print(MyMap)
Visited = [0]*(V+1)
Distance = [INF]*(V+1)


for i in range(V+1):
    if MyMap[i] :
        Distance[i] = MyMap[Start][i]

for _ in range(V):
    Shortest = getMin()
    Visited[Shortest] = True

    for now in range(V+1):
        if Distance[now] > Distance[Shortest] + MyMap[Shortest][now]:
            Distance[now] = Distance[Shortest] + MyMap[Shortest][now]
    Distance[Start] = 0

for i in range(Start, V+1):
    print(Distance[i],'')
