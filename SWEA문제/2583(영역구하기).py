import sys
sys.stdin = open('../영역구하기.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(x, y):
    area = 1
    queue = [(x, y)]
    matrix[x][y] = 1
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] == 0:
                queue.append((nx, ny))
                matrix[nx][ny] = 1
                area += 1
    return area

m, n, k = map(int, input().split())
matrix = [[0]*n for _ in range(m)]
for _ in range(k):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 1

result = []
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            result.append(bfs(i, j))

print(len(result))
for i in sorted(result):
    print(i, end=' ')
