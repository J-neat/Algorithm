import sys
sys.stdin = open('Contact.txt', 'r')

def bfs(start):
    q = [start]
    visited[start] = 1

    while q:
        node = q.pop(0)
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = visited[node] + 1
                q.append(i)

for _ in range(10):
    N, start = map(int, input().split())
    temp = list(map(int, input().split()))
    graph = [[] for _ in range(101)]
    visited = [0 for _ in range(101)]

    for i in range(0, len(temp), 2):
        graph[temp[i]].append(temp[i+1])

    bfs(start)

    max_value = max(visited)
    answer = [i for i, value in enumerate(visited) if value == max_value]

    print(f'#{_+1} {max(answer)}')
