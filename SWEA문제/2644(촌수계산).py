import sys
sys.stdin = open('../촌수계산.txt', 'r')

def BFS(start, end):
    queue = [start]
    visited = [0 for _ in range(n+1)]
    while queue:
        current = queue.pop(0)
        if current == end:
            return visited[current]
        for i in graph[current]:
            if visited[i] == 0:
                visited[i] = visited[current] + 1
                queue.append(i)
    return -1

n = int(sys.stdin.readline())
start, end = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

print(BFS(start, end))
