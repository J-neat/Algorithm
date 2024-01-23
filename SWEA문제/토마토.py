import sys
sys.stdin = open('토마토.txt', 'r')

M, N, H = map(int, input().split())
MyList = [[list(map(int, input().split())) for __  in range(N)] for ___ in range(H)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(queue):
    day = -1
    while queue:
        day += 1
        for _ in range(len(queue)):
            x, y, z = queue.pop(0)
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and MyList[nx][ny][nz] == 0:
                    MyList[nx][ny][nz] = 1
                    queue.append((nx, ny, nz))
    return day

queue = []
for i in range(H):
    for j in range(N):
        for k in range(M):
            if MyList[i][j][k] == 1:
                queue.append((i, j, k))

result = bfs(queue)

for i in range(H):
    for j in range(N):
        for k in range(M):
            if MyList[i][j][k] == 0:
                print(-1)
                exit(0)
#위에 print(result) 넣으면 루프 발생함


print(result)
