def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    for idx in range(n):
        if visited[idx] == 0:
            dfs(n, computers, visited, idx)
            answer += 1
    return answer

def dfs(n, computers, visited, idx):
    visited[idx] =1
    for next in range(n):
        if idx != next and computers[idx][next] == 1:
            if visited[next] == 0:
                dfs(n, computers, visited, next)