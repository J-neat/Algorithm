import sys
sys.stdin = open('단지번호붙이기.txt', 'r')

N = int(input())

graph = [list(map(int, input())) for _ in range(N)]
Visited = [[0]*N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    queue = [(x,y)]
    Visited[x][y] = 1
    count = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and Visited[nx][ny] == 0:
                queue.append((nx, ny))
                Visited[nx][ny] = 1
                count += 1
    return count

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and Visited[i][j] ==0:
            result.append(bfs(graph, i, j))

print(len(result))
for r in sorted(result):
    print(r)