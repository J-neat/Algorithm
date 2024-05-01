from collections import deque
def solution(maps):
    answer = 0
    m = len(maps[0])
    n = len(maps)
    visited = [[0] * m for _ in range(n)]
    queue = deque([(0, 0, 1)])
    visited[0][0] = 1
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        x, y, dist = queue.popleft()
        
        if x == n-1 and y == m-1:
            return dist
        
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, dist+1))
    return -1