answer = 0
def solution(n, computers):
    global answer
    visited = [0 for i in range(n)]
    for idx in range(n):
        if visited[idx] == 0:
            dfs(n, computers, idx, visited)
            answer += 1
    return answer

def dfs(n, computers,idx, visited):
    visited[idx] = 1
    for next in range(n):
        if idx != next and computers[idx][next] == 1:
            if visited[next] == 0:
                dfs(n, computers, next, visited)
    
            
    