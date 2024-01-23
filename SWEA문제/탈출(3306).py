import sys
sys.stdin = open('탈출.txt', 'r')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def flood_fill():
    num = len(water)
    for _ in range(num):
        x, y = water.pop(0)
        for direction in range(4):
            nx, ny = x + dx[direction], y + dy[direction]
            if (0 <= nx < N) and (0 <= ny < M):
                if field[nx][ny] not in ['D', 'X', '*']:
                    field[nx][ny] = '*'
                    water.append((nx, ny))

def move_hedgehog():
    num = len(hedgehog)
    for _ in range(num):
        x, y = hedgehog.pop(0)
        for direction in range(4):
            nx, ny = x + dx[direction], y + dy[direction]
            if (0 <= nx < N) and (0 <= ny < M):
                if field[nx][ny] == 'D':
                    return visit[x][y] + 1
                if field[nx][ny] == '.':
                    field[nx][ny] = 'S'
                    visit[nx][ny] = visit[x][y] + 1
                    hedgehog.append((nx, ny))
    return -1

N, M = map(int, input().split())
field = [list(input()) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
water = []
hedgehog = []

for i in range(N):
    for j in range(M):
        if field[i][j] == 'S':
            hedgehog.append((i, j))
        if field[i][j] == '*':
            water.append((i, j))

while True:
    flood_fill()
    result = move_hedgehog()
    if result != -1:
        print(result)
        break
    if not hedgehog:
        print('KAKTUS')
        break
