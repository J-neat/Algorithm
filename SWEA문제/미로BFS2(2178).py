import sys
sys.stdin = open('미로BFS2(2178).txt', 'r')

N, M = map(int, input().split()) # N = 4, M = 6
MyList = [list(map(int, input())) for _ in range(N)]
Visited = [[0]*M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
end = (N-1, M-1)  # Python uses 0-based indexing

def bfs(end):
    graph = [(0, 0)]  # Start from (0,0)
    Visited[0][0] = 1  # Mark the start node as visited
    while graph:
        x, y = graph.pop(0)
        if (x, y) == end:
            return Visited[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and MyList[nx][ny] == 1 and Visited[nx][ny] == 0:
                graph.append((nx, ny))
                Visited[nx][ny] = Visited[x][y] + 1  # Keep track of the distance

print(bfs(end))
