import sys
sys.stdin = open("미로의거리.txt", "r")
T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maze, start):
    N = len(maze)
    visited = [[0] * N for _ in range(N)]
    queue = [start]
    visited[start[0]][start[1]] = 1

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            newX, newY = x + dx[i], y + dy[i]
            if newX < 0 or newX >= N or newY < 0 or newY >= N or maze[newX][newY] == '1':
                continue
            if maze[newX][newY] == '3':
                return visited[x][y] - 1
            if not visited[newX][newY] or maze[newX][newY] == '0':
                queue.append((newX, newY))
                visited[newX][newY] = visited[x][y] + 1
    return 0

for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    start = [(i, j) for i in range(N) for j in range(N) if maze[i][j] == '2'][0]
    print(f"#{test_case} {bfs(maze, start)}")
