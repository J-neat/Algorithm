from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    q = deque()
    direction = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    visited = [[1 for _ in range(102)]for __ in range(102)]
    graph = [[-1 for _ in range(102)]for __ in range(102)]
    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, rect)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1#테두리 1, 내부0, 외부 -1
                    
                    
    cx, cy, ix, iy = 2*characterX, 2*characterY, 2*itemX, 2*itemY
    q.append([cx, cy])
    while q:
        x, y = q.popleft()
        
        if x == ix and y == iy:
            answer = visited[x][y]
            break
            
        for k in range(4):
            nx, ny = x + direction[k][0], y + direction[k][1]
            if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[x][y]
                q.append([nx, ny])
    return (answer-1)//2