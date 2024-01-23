import sys
sys.stdin = open('나이트의이동.txt', 'r')

T = int(input())

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def bfs(I, start, end):
    queue = [start + [0]]  # start position and count
    visited = [[False]*I for _ in range(I)]
    visited[start[0]][start[1]] = True
    while queue:
        x, y, count = queue.pop(0)
        if [x, y] == end:
            return count
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny, count + 1])

for _ in range(T):
    I = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print(bfs(I, start, end))
