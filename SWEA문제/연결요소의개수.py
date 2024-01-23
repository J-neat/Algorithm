import sys
sys.stdin = open('연결요소의개수.txt', 'r')

N, M = map(int, input().split())
Visited = []
MyList = [[0 for _ in range(N)] for __ in range(N)] # NxN의 리스트


for i in range(M):
    a, b = map(int, input().split())
    MyList[a-1][b-1]= 1
    MyList[b-1][a-1] = 1

def bfs(v, Visited):#v는 시작점
    queue = [v]#큐에 시작 점 추가
    while queue:#큐가 빌 때 까지 반복하는 것임
        v = queue.pop(0)
        for i in range(N):
            if MyList[v][i] == 1 and i not in Visited:
                queue.append(i)
                Visited.append(i)#방문했다고 체크 해놓기


count = 0
for i in range(N):
    if i not in Visited:
        bfs(i, Visited)
        count += 1

print(count)