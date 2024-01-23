import sys
sys.stdin = open("노드구하기.txt", "r")
T = int(input())
def bfs(graph, start, end):
    visited = [0 for _ in range(len(graph))]
    queue = [start]
    visited[start] = 1

    while queue:
        v = queue.pop(0)
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                queue.append(i)
    if visited[end]:
        return visited[end] -1
    else :
        return 0

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)
    S, G = map(int, input().split())

    result = bfs(graph, S, G)
    print(f"#{test_case} {result}")
