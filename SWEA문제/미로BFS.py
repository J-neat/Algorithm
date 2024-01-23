#미로 BFS
import sys
sys.stdin = open('../input2.txt', 'r')

row, col = map(int, input().split())
MyMap = []
Queue = []
Visited = [[0]*col for _ in range(row)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def isPossible(y, x):
    if (0 <= y < 5 and 0 <= x < 5 and MyMap[y][x] != '#' and not Visited[y][x]):
        return True
    else:
        return False

for _ in range(row):
    MyMap.append(input())

for y in range(5):
    for x in range(5):
        if MyMap[y][x] == 'S':
            startY = y
            startX = x
            Queue.append([startY, startX])
            Visited[startY][startX] = True


while Queue:
    y, x = Queue.pop(0)
    if MyMap[y][x] == 'G':
        print("End")
    for dir in range(4):
        newY = y + dy[dir]
        newX = x + dx[dir]
        if isPossible(newY, newX):
            Visited[newY][newX] = True
            Queue.append([newY, newX])
