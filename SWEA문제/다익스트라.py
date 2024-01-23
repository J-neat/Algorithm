import sys
sys.stdin = open('다익스트라.txt', 'r')

def getMin():
    min = INF
    whereMin = -1
    for now in range(V+1):
        if not Visited[now] and Distance[now] < min:
            min = Distance[now]
            whereMin = now
    return whereMin

INF = int(1e9)##엄청 큰 숫자를 표현 /INF = 987654321 사용해도 괜찮다.
V, E = map(int, input().split())
MyMap = [[INF]*(V+1)for _ in range(V+1)]

for _ in range(E):
    start, stop, cost = map(int, input().split())
    MyMap[start][stop] = cost

Visited = [0]*(V+1)

start = 0
Distance = [INF]*(V+1)

Distance[start] = 0

for i in range(V+1):
    if MyMap[i] : Distance[i] = MyMap[0][i]##MyMap[i]가 0 이 아니면 Distance[i] = MyMap[i]이렇게 해라

for _ in range(V):
    Shortest = getMin()
    Visited[Shortest] = True

    for now in range(V+1):##now == 1 9
        if Distance[now] > Distance[Shortest] + MyMap[Shortest][now]:
            Distance[now] = Distance[Shortest] + MyMap[Shortest][now]
        print(Distance)