import sys
sys.stdin = open('유기농배추.txt', 'r')

#인접해 있는지 검사 하는 것

N, M, K = map(int, input().split())

myList = [[0 for j in range(N)] for i in range(M)]

for i in range(K):
    m, n = map(int, input().split())#m이 x n 이 y
    myList[n][m] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = [(x, y)]
    myList[y][x] = 0

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny <0 or nx >= N or ny >= M:
                continue

            if myList[ny][nx] == 1:
                queue.append((nx, ny))
                myList[ny][nx] = 0

count = 0
for i in range(M):
    for j in range(N):
        if myList[i][j] == 1:
            bfs(j, i)
            count += 1

print(count)

